from flask import *
from werkzeug.security import check_password_hash, generate_password_hash
from utils.func import *
import sqlite3

login_manager = LoginManager()

# Fazendo a aplicação
app = Flask(__name__)

login_manager.__init__(app)

app.secret_key = '20r0]5/reyg1@S*v*FZJ58HnH1=oAy{t<6<rx]A(QdPBq(")*Lsd"HbJgPSpVbT'

@login_manager.user_loader
def load_user(user_id):
    '''Retorna o email do usuário, que é definido como chave única'''
    return User.get(user_id)



# Primeira rota. Tentando visualizar o footer e posteriormente a header
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Rota para cadastro do usuário. Caso ele não tenha um user, ele será cadastrado. Caso possua um identificador presente no banco de dados,
    ele será redirecionado para a página de login.'''

    if request.method == 'POST':
        # Coletando os dados do formulário
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Estabelecendo a conexão. Função da pasta utils, arquivo func.py
        conn = get_conexion()

        # Verificando se o user existe no database a partir de seu identificador, o email.
        sql = "SELECT * FROM users WHERE email = ?"
        result = conn.execute(sql, (email,)).fetchone()

        if not result:
            '''Se retornar None: fazendo o cadastro 
            caso o email não esteja no banco de dados'''
            
            # Fazendo a password_hash com werkzeug
            password_hash = generate_password_hash(password)

            #(default, username, email, password_hash, default, default)"
            sql = "INSERT INTO users(username, email, password_hash) VALUES(?, ?, ?)"
            
            conn.execute(sql, (username, email, password_hash))
            conn.commit()

            user = User(email=email, password_hash=password_hash)
            user.id = email

            login_user(user)

            return redirect(url_for('index'))
        
        else:
            flash('Você já tem cadastro, faça login', category='error')
            return redirect(url_for('index'))
    
    # Se o método for GET
    return render_template('register.html')


# Rota de Login