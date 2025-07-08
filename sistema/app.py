import sqlite3


# Abrindo uma conexão
conn = sqlite3.connect('banco.db')
SCHEMA = 'schema.sql'

# 

# Para executar isso, é preciso estar localizado na pasta models
with open(SCHEMA) as f:
    conn.executescript(f.read())

# Fechando a conexão
conn.close()