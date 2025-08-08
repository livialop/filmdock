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


# start_database('../schema.sql') # Falta implementar isso depois


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
        conn = get_connection()

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
            flash('Cadastro realizado com sucesso!', category='success')

            close_connection()  # Fechando a conexão com o banco de dados

            return redirect(url_for('films'))  # Redirecionando para a página de filmes
        
        else:
            flash('Você já tem cadastro, faça login', category='error')
            return redirect(url_for('login'))  # Redirecionando para a página de login
    
    # Se o método for GET
    return render_template('register.html')


# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        sql = "SELECT * FROM users WHERE email = ?"
        result = conn.execute(sql, (email,)).fetchone()

        if not result:
            flash('Usuário não logado', category='error')
            return redirect(url_for('register'))
        
        elif result:
            sql_get_password = "SELECT * FROM users WHERE email = ?"
            result_password = conn.execute(sql_get_password, (email,)).fetchone()

            pwrdcheck = check_password_hash(pwhash=result_password[3], password=password)
            
            # if result_password[3] != check_password_hash(result_password[3], password):
            if not pwrdcheck:
                flash('Senha incorreta', category='error')
                return redirect(url_for('login'))
            
            else:
                user = User(email=email, password_hash=result_password[3])
                user.id = email
                login_user(user)

                flash('Você está logado!', category='success')
                return redirect(url_for('films')) 
            
        close_connection()  # Fechando a conexão com o banco de dados

    # Se o método for GET
    return render_template('login.html')

@app.route('/films', methods=['GET', 'POST'])
@login_required # Apenas usuários logados podem acessar essa rota
def films():
    '''Páginas para o usuário ter a opção de logar um filme e visualizar aqueles que já foram logados.
        Estrutura pensada: 
        -> Pegar título do filme, ano.
        -> Se o usuário clicar, isso expande para a tela onde ele poderá ver sua review e avaliação.
    '''
    conn = get_connection()
    sql_get_film_data = "SELECT title, year, rating, review FROM film_user WHERE user_email = ?"
    # dict: {titulo: (ano, avaliação, review)}

    try:
        films = conn.execute(sql_get_film_data, (current_user.id,)).fetchall() 
        films_data = {}
        for film in films:
            films_data[film[0]] = {
                'year': film[1],
                'rating': film[2],
                'review': film[3]
            }
        # print(films_data) # Checando o que está sendo retornado, comentar isso depois.
        close_connection()  # Fechando a conexão com o banco de dados

    except sqlite3.Error as e:
        print(e)
        flash(f'Erro ao acessar o banco de dados: {e}', category='error')
        return redirect(url_for('index'))

    return render_template('films.html', films_name=list(films_data.keys()), films_data=films_data)


@app.route('/add_films', methods=['GET','POST'])
@login_required # Apenas usuários logados podem acessar essa rota
def add_films():
    '''Rota onde o usuário irá adicionar um filme'''
    if request.method == 'POST':
        film_title = request.form.get('title')
        film_year = request.form.get('year')
        film_review = request.form.get('review')
        # Making sure that the rating is a integer between 1-5
        try:
            film_rating = int(request.form.get('rating'))
            if film_rating < 1 or film_rating > 5:
                raise ValueError('Avaliação deve ser entre 1 e 5.')
        except (ValueError, TypeError):
            flash('A avaliação deve ser um número inteiro entre 1 e 5.', category='error')
            return redirect(url_for('add_films'))

        # Checando campos obrigatórios
        if not film_title or not film_rating:
            flash('O título do filme e sua avaliação são obrigatórios.', category='error')
            return redirect(url_for('add_films'))
        
        try:
            conn = get_connection()
            sql_insert_film = "INSERT INTO film_user (user_email, title, year, rating, review) VALUES (?, ?, ?, ?, ?)"

            conn.execute(sql_insert_film, (current_user.id, film_title, film_year, film_rating, film_review))
            conn.commit()

            flash('Filme adicionado!', category='success')
            close_connection()  # Fechando a conexão com o banco de dados
            return redirect(url_for('films'))
        
        except Exception as e:
            conn.rollback() # Se der errado, o banco de dados volta para um ponto anterior
            flash('Erro ao adicionar o filme.', category='error')
            return redirect(url_for('add_films'))
    

    # Se o método for GET
    return render_template('add_films.html')


@app.route('/logout')
@login_required 
def logout():
    '''Rota para deslogar o usuário'''
    logout_user()
    flash('Você foi deslogado com sucesso!', category='success')
    return redirect(url_for('index'))

# Rotas de erro

@app.errorhandler(404)
def page_not_found(error):
    '''Rota personalizada para o erro 404 '''
    return render_template('error/404.html'), str(error)

@app.errorhandler(500)
def internal_server_error(error):
    '''Rota personalizada para o erro 500'''
    return render_template('error/500.html'), str(error)

@app.errorhandler(Exception)
def handle_generic_exception(error):
    response = {
        "error": "Unexpected Error",
        "message": "An unknown error has occurred. Please try again later.",
        "status": 500
    }
    return render_template('error/generic.html', response), str(error)