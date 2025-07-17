from flask import * 
from flask_login import *

import sqlite3

def get_conexion():
    '''Função para realizar a conexão com o banco de dados'''
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn 


class User(UserMixin):
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
