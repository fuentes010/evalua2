from flask import request, redirect, render_template, url_for, json, jsonify
from app import app
from models import bloom_category,bloom_category_rev,bloom_value,ra_value

COLORS = {
            1:"#2980b9",
            2:"#90C695",
            3:"#F5D76E",
            4:"#F5D76E",
            5:"#DADFE1",
            6:"#F5AB35",
            }
HIGHLIGHTS = {
                1:"#446CB3",
                2:"#26A65B",
                3:"#96281B",
                4:"#F7CA18",
                5:"#DADFE1",
                6:"#F39C12",
            }


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get_bloom_stats', methods=['POST'])
def get_bloom_stats():
    #Obtenemos la version de bloom.
    bloom_version = request.data or 'bloom'
    values_bloom = bloom_value.query.all()

    if bloom_version == 'bloom':
        categories_bloom = bloom_category.query.order_by(bloom_category.seq)
        values_bloom_dict = {v.id:{'name':v.name.lower(),'categ_id':v.categ_id} for v in values_bloom}
    else:
        categories_bloom = bloom_category_rev.query.order_by(bloom_category_rev.seq)
        values_bloom_dict = {v.id:{'name':v.name.lower(),'categ_id':v.categ_rev_id} for v in values_bloom}
    #Creamos un diccionario ya preparado para devolver a la libreria que va a pintar las graficas
    categories_totals = {
                         b.id:{"value": 0,
                               "color":COLORS[b.id],
                               "highlight": HIGHLIGHTS[b.id],
                               "label": b.name}
                         for b in categories_bloom}


    ra_values = ra_value.query.all()
    #Por cada uno de los resultados de aprendizaje
    for ra in ra_values[:200]:
        #Creamos un diccionario clasificando las palabras con las categorias a las que pertenece
        for val_id, val_dict in values_bloom_dict.items():
            if val_dict['name'] in ra.NOMBRE.lower():
                categories_totals[val_dict['categ_id']]['value'] += 1
    res = {
            'total_ra':200,
            'values': categories_totals.values()
            }

    return jsonify(res);

@app.route("/bloom")
def bloom():
    #Obtenemos todos los valores para poder construir la tabla
    categories_bloom = bloom_category.query.order_by(bloom_category.seq)
    categories_totals = {b.id:{'name':b.name,'qty':0} for b in categories_bloom}
    values_bloom = bloom_value.query.all()
    values_bloom_dict = {v.id:{'name':v.name.lower(),'categ_id':v.categ_id} for v in values_bloom}
    return get_data(categories_bloom, values_bloom_dict)

@app.route("/bloom_revisado")
def bloom_revisado():
    #Obtenemos todos los valores para poder construir la tabla
    categories_bloom = bloom_category_rev.query.order_by(bloom_category_rev.seq)
    categories_totals = {b.id:{'name':b.name,'qty':0} for b in categories_bloom}
    values_bloom = bloom_value.query.all()
    values_bloom_dict = {v.id:{'name':v.name.lower(),'categ_id':v.categ_rev_id} for v in values_bloom}
    return get_data(categories_bloom, values_bloom_dict)

def get_data(categories_bloom,values_bloom_dict):
    categories_totals = {b.id:{'name':b.name,'qty':0} for b in categories_bloom}
    ra_values = ra_value.query.all()
    #Por cada uno de los resultados de aprendizaje
    result = []
    res_append = result.append
    for ra in ra_values[:200]:
        #Creamos un diccionario con las categorias de bloom
        #y las veces que aparece una palabra de esa categoria inicializadas a 0
        bloom = {b.id:{'name':b.name,'qty':0,'seq':b.seq} for b in categories_bloom}

        #Creamos un diccionario clasificando las palabras con las categorias a las que pertenece
        appearences_dict = {}
        for val_id, val_dict in values_bloom_dict.items():
            if val_dict['name'] in ra.NOMBRE.lower():
                bloom[val_dict['categ_id']]['qty'] += 1
                categories_totals[val_dict['categ_id']]['qty'] += 1
                try:
                    if bloom[val_dict['categ_id']]['name'] not in appearences_dict[val_dict['name']]:
                        appearences_dict[val_dict['name']].append(bloom[val_dict['categ_id']]['name'])
                except KeyError:
                    appearences_dict[val_dict['name']] = [bloom[val_dict['categ_id']]['name']]

        #Dividimos la frase en palabras y buscamos si es una palabra de la taxonomia de bloom
        resut_phrase = []
        for woord in ra.NOMBRE.split(' '):
            if woord.lower() in appearences_dict.keys():
                #En caso afirmativo le activamos un tooltip con las categorias a las que pertece
                resut_phrase.append("<span class='bg-green tooltipped' data-position='right' data-delay='5' data-tooltip='%s'>%s</span>" % ((', ').join(appearences_dict[woord.lower()]),woord))
            else:
                resut_phrase.append(woord)

        res_append([(' ').join(resut_phrase),sorted(bloom.items(), key=lambda (x, y): y['seq'])])

    return render_template('results.html',categories_bloom=categories_bloom,ra_values=result)
