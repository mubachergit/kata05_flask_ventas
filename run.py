from flask import Flask, render_template, request
import csv, sqlite3

app = Flask(__name__)
BASE_DATOS = './data/ventas.db'

@app.route("/")
def index():
    fVentas = open('./sales.csv', 'r')
    csvreader = csv.reader(fVentas, delimiter=',')
    print('hola')

    d = {}   
    for linea in csvreader:
        if linea[0] in d:
            d[linea[0]]['ingresos'] += float(linea[11])
            d[linea[0]]['beneficios'] += float(linea[13])
        else:
            if linea[0] != 'region':
                d[linea[0]] = {'ingresos':float(linea[11]), 'beneficios':float(linea[13])}


    return render_template('region.html',ventas=d)

@app.route("/paises")
def paises():
    region_name = request.values["region"]

    fVentas = open('./sales.csv', 'r')
    csvreader = csv.reader(fVentas, delimiter= ',')
    d = {}
    for linea in csvreader:
        if linea[0] == region_name:
            if linea[1] in d:
                d[linea[1]]['ingresos'] += float(linea[11])
                d[linea[1]]['beneficios'] += float(linea[13])
            else:
                d[linea[1]] = {'ingresos':float(linea[11]), 'beneficios':float(linea[13])}

    return render_template('pais.html',ventas=d, region_nm=request.values['region'])

@app.route("/productos")
def productos():
    conn = sqlite3.connect(BASE_DATOS)
    cur = conn.cursor()
    
    query = "SELECT id, tipo_producto, precio_unitario, coste_unitario FROM productos;"
    productos = cur.execute(query).fetchall()

    conn.close()
    return render_template ('productos.html', productos=productos)

@app.route("/addproducto")
def addProduct():
    return render_template ('newproduct.html')