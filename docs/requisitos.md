# Documento de Requisitos Funcionais - FilmDock

**Tema**: Sistema para logar filmes assistidos com reviews e pontuações.


## 1. Cadastro e autenticação

- **RF01**: Usuário poderá criar conta com e-mail e senha.
- **RF02**: Usuário poderá fazer login/logout.
- **RF03**: Senhas serão armazenadas com hash (*werkzeug security*).


## 2. Gerenciamento de filmes e reviews

- **RF04**: Usuário poderá adicionar um filme assistido, informando título, data assistida, gênero, pontuação (opcional) e review (opcional).
- **RF05**: Usuário poderá visualizar todos os filmes logados por ele, com opção de visualização detalhada (incluindo review e pontuação).
- **RF06**: Usuário poderá editar a pontuação e a review de um filme já logado.
- **RF07**: Usuário poderá excluir um filme do seu histórico.
- **RF08**: Usuários não podem interagir entre si, sendo esse sistema um software de uso individual.


## 3. Gerenciamento de perfil do usuário

- **RF09**: Usuário poderá editar informações do perfil, como foto, nome e outros dados pessoais.
- **RF10**: Usuário poderá visualizar seu perfil com informações atualizadas.


## 4. Banco de Dados

- **RF11**: Usar SQLite para armazenar dados de usuários, filmes e reviews.
<!-- - **RF12**: Tabelas adequadas para usuários (id, nome, e-mail, senha_hash, foto, etc.) e filmes (id, título, data_assistida, pontuação, review, user_id, etc.). -->


## 5. Templates e navegação

- **RF13**: Uso de `extends` e `includes` para layout base (navbar, footer) e páginas específicas.
- **RF14**: Página inicial (homepage) apresentando o sistema, com opções de cadastro/login.
- **RF15**: Página pessoal do usuário com histórico de filmes logados e mensagem caso não haja registros.
- **RF16**: Página de adição/edição de filmes com formulário intuitivo.
- **RF17**: Páginas de erro personalizadas (404 e 500).


## 6. Requisitos Técnicos

- **RF18**: Uso de `request` para processar formulários de cadastro, login e filmes.
- **RF19**: Uso de `redirect` e `url_for` para navegação entre páginas.
- **RF20**: Uso de `make_response` para cookies ou headers customizados, se necessário.
- **RF21**: Código versionado no GitHub com entregas semanais conforme cronograma.
- **RF22**: README detalhado com instruções de instalação, dependências e screenshots.


## 7. Fluxo do sistema

1. **Página inicial**: Apresenta o FilmDock e opções de cadastro/login.
2. **Cadastro/login**: Usuário cria conta ou faz login.
3. **Página pessoal**: Exibe histórico de filmes logados ou mensagem "Nenhum filme registrado".
4. **Adicionar filme**: Formulário para preencher título, data, gênero, pontuação e review.
5. **Editar/excluir filme**: Opções disponíveis para cada filme listado.
6. **Perfil do usuário**: Permite editar informações pessoais.
---

