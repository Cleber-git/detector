from flask import Flask, jsonify, request
import sqlite3

con = sqlite3.connect("base.db")

cur = con.cursor()

res = cur.execute("Select nome from ListaAcademias")
res.fetchall() 

print(res.fetchall() )

app = Flask(__name__)

# Dados em memória (para exemplificação)
items = ["Cachorro", "Gato", "Galinha", "Coelho"]

# Endpoint para listar todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200



if __name__ == '__main__':
    app.run(debug=True)
