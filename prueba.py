import sqlite3
import csv

conn = sqlite3.connect('./data/ventas.db')

fVentas = open('./sales10.csv', 'r')
csvreader = csv.reader(fVentas, delimiter= ',')

c = conn.cursor()
for linea in csvreader:
    c.execute( '''CREATE TABLE productoss
                    (id INTEGER UNIQUE,
                    tipo_producto TEXT NOT NULL UNIQUE,
                    precio_unitraio REAL NOT NULL,
                    coste_unitario REAL NOT NULL)''' )
    print(linea)
    
    