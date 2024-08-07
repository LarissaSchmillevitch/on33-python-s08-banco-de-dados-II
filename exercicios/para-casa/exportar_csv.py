import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(registros)

cursor.close()
conn.close()
