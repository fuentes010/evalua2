# -*- coding: utf-8 -*-

import csv
import psycopg2
from pprint import pprint

conn = psycopg2.connect(database="evalua2", user="pablo", password="", host="127.0.0.1", port="5432")
cur = conn.cursor()


def valores_bloom():
    cur.execute('DELETE FROM core_categoriabloomvalor')
    conn.commit()
    cur.execute('SELECT * FROM bloom_value')
    insert = """INSERT INTO core_categoriabloomvalor (id, name, categ_id_id) VALUES """
    vals = []
    for v in cur.fetchall():
        vals.append("(%s, '%s', %s)" % (v[0], v[2], v[1]))
    cur.execute(insert + ', '.join(vals))
    conn.commit()
    conn.close()


def resultado_aprendizaje():
    cur.execute('DELETE FROM core_resultadoaprendizaje')
    conn.commit()
    cur.execute('SELECT * FROM ra_value')
    insert = "INSERT INTO core_resultadoaprendizaje (name) VALUES "
    vals = []
    for v in cur.fetchall():
        vals.append("('%s')" % v[1].replace("'", "''"))

    cur.execute(insert + ', '.join(vals))
    conn.commit()
    conn.close()


def cursos_etsinf_grado():
    cur.execute('DELETE FROM core_asignatura')
    conn.commit()
    fil = csv.reader(open("asig.csv","rb"), delimiter=";")
    insert = "INSERT INTO core_asignatura (id, name, curso_id_id) VALUES "
    vals = []
    vkeys = []
    idx = 1
    for curso in fil:
        if int(curso[1]) > 0:
            vkey = "('%s', %s)" % (curso[0].replace("'", "''"), curso[1])
            if vkey not in vkeys:
                vals.append("(%s , '%s', %s)" % (idx, curso[0].replace("'", "''").strip(), curso[1]))
                idx += 1
                vkeys.append(vkey)

    cur.execute(insert + ', '.join(vals))
    conn.commit()
    conn.close()

def res_aprend_asignatura():
    cur.execute('DELETE FROM core_resultadoaprendizaje')
    conn.commit()
    insert = "INSERT INTO core_resultadoaprendizaje (id, name, asig_id_id) VALUES "
    fil = csv.reader(open("rel_apren.csv", "rb"), delimiter=";")
    vals = []
    idx = 1
    for res_apren in fil:
        cur.execute("SELECT id, name FROM core_asignatura where name like '"+res_apren[1].replace("'", "''").strip()+"%'")
        res = cur.fetchall()
        ass_id = res[0][0]
        vals.append("(%s , '%s', %s)" % (idx, res_apren[0].replace("'", "''").strip(), ass_id))
        idx += 1

    cur.execute(insert + ', '.join(vals))
    conn.commit()
    conn.close()


res_aprend_asignatura()
