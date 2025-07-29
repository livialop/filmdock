from flask import * 
from flask_login import *

import sqlite3
import subprocess

def get_conexion():
    '''Função para realizar a conexão com o banco de dados'''
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn 


def start_database(file):
    '''Função para iniciar o banco de dados, podendo ser utilizada direto na aplicação.
    Isso diminui a repetição de estar sempre procurando qual arquivo executar quando alguma
    alteração é feita no banco de dados.'''
    try:
        result = subprocess.run(['python', file], capture_output=True, text=True, check=True)
        print(result.stdout) # Imprime a saída do arquivo executado
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o arquivo: {e}")
        print(e.stderr) # Imprime o erro, se houver


class User(UserMixin):
    '''Classe para definir o usuário na aplicação'''
    def __init__(self, email, password_hash) -> None:
        self.email = email
        self.password_hash = password_hash

    @classmethod
    def get(cls, user_id):
        '''user_id: Email do usuário como chave única'''
        conexao = get_conexion()
        sql = "SELECT * FROM users WHERE email = ?"
        resultado = conexao.execute(sql, (user_id,)).fetchone()
        if resultado:
            user = User(email=resultado['email'], password_hash=resultado['password_hash'])
            user.id = resultado['email']
            return user
