from flask import Flask
from sqlalchemy import SQLAlchemy
import mysql.connector

# Conexão direta com o MySQL usando mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='virtualtech',
)

cursor = conexao.cursor()

app = Flask(__name__)

# Configuração do SQLAlchemy, codificando o caractere especial na senha
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativar notificações de alterações

db = SQLAlchemy(app)

# Exemplo de modelo
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return "Plataforma de Tarefas Colaborativas"

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados


#CRUD
#comando = ''
#cursor.execute(comando)
#conexao.commit() Para editar o banco de dados
#resultado = cursor.fetchall() para ler o banco de dados 

#CREATE
# comando = f'INSERT INTO produto(nome, marca) VALUES ("TV", "Samsung")'
# cursor.execute(comando)
# conexao.commit()

#READ
# comando = f'SELECT * FROM produto'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#UPDATE
# comando = f'UPDATE produto SET preco = 4999.99 WHERE nome = "TV"'
# cursor.execute(comando)
# conexao.commit()

#DELETE
# comando = f'DELETE FROM produto WHERE preco = 5000.00'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()