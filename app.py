from flask import Flask, jsonify, request
import sqlite3

con = sqlite3.connect("base.db")

cur = con.cursor()

res = cur.execute("Select nome, cidade, bairro, rua from ListaAcademias")
readAll = res.fetchall()

model = {
    readAll[0][0]:{
        'cidade'   :readAll[0][1],
        'bairro'   :readAll[0][2],
        'rua'      :readAll[0][3]
        },
    readAll[1][0]:{
        'cidade'   :readAll[1][1],
        'bairro'   :readAll[1][2],
        'rua'      :readAll[1][3]
        },
    readAll[2][0]:{
        'cidade'   :readAll[2][1],
        'bairro'   :readAll[2][2],
        'rua'      :readAll[2][3]
        }
}

# print(model)
# for m in model:
#     if "Augusta" == m:
#         print(model.get(m))
    
app = Flask(__name__)

# Endpoint para listar todos os itens
@app.route('/<academia>', methods=['GET'])
def get_items(academia):
    erro = {'erro': "Não encontrado"}
    for m in model:
        if academia in m:
            return jsonify(model.get(m))
        
    return jsonify(erro), 404
    

if __name__ == '__main__':
    app.run(debug=True)
