from flask import *

import sqlite3

# Fazendo a aplicação
app = Flask(__name__)


# Abrindo uma conexão
conn = sqlite3.connect('banco.db')
SCHEMA = 'schema.sql'

# 

# Para executar isso, é preciso estar localizado na pasta models
with open(SCHEMA) as f:
    conn.executescript(f.read())

# Primeira rota. Tentando visualizar o footer e posteriormente a header
@app.route('/')
def index():
    return render_template('index.html')


# Fechando a conexão
conn.close()