# -*- coding: utf-8 -*-

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

resultado_aprendizaje()
