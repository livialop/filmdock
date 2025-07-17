import sqlite3

# Abrindo uma conexão
conn = sqlite3.connect("banco.db")
SCHEMA = 'schema.sql'

# Criação de tabelas
with open(SCHEMA) as f:
    conn.executescript(f.read())

# Fechando a conexão
conn.close()

# Abrindo uma conexão
conn = sqlite3.connect('banco.db')
SCHEMA = 'schema.sql'