# FilmDock

## O que é o FilmDock?
O FilmDock é um projeto desenvolvido para a matéria de Programação de Sistemas para Internet (PSI) que consiste em um sistema para logar filmes assistidos com reviews e pontuações. Posteriormente, será desenvolvido como um projeto pessoal meu.

> [!NOTE]
> Esse projeto foi feito individualmente, o único contribuidor fui eu (Lívia Lopes).

## Como posso rodar localmente este projeto?
O FilmDock foi feito utilizando o framework ```Flask``` para fazer a aplicação. Caso seja de seu interesse rodar esse projeto localmente, siga os seguintes passos:
1. Clone este repositório. Você pode fazer isso utilizando o comando:
```cmd
git clone https://github.com/livialop/filmdock.git
```

2. Crie um ambiente virtual e em seguida, instale as dependências do projeto. Para instalar todos os requerimentos, utilize o comando:
```cmd
pip install -r requirements.txt
```
> [!TIP]
> Se não sabe como utilizar ambientes virtuais, fiz um guia de como usar para cada SO. Clique [aqui](https://github.com/livialop/Banquinho/blob/0392a9d2e27a8a821bd22dfddabd6ea8285e1d6e/wikis/ambientesvirtuais.md) para ser redirecionado.

3. Navegue até a pasta ```src/``` do repositório e digite no terminal ```flask run --debug```. Isso iniciará a aplicação.

Caso você opte por não criar uma conta e utilizar um usuário mock, logue com as seguintes credenciais:
* Email: liv@gmail.com
* Password: 123

> [!CAUTION]
> Não utilize dados reais na aplicação, pois o banco de dados está público para que todos possam ver. Ele está assim momentaneamente para a avaliação do projeto.

## Funcionamento do projeto, páginas


## Navegação pelo repositório
<details>
  <summary>Documentos</summary>
    <ul>
        <li><a href='docs/requisitos.md'>Requisitos Funcionais</a></li>
        <li><a href='docs/orgsemanal.md'>Organização Semanal</a></li>
        <li><a href='docs/encaminhamentos.md'>Encaminhamentos</a></li>
    </ul>
</details>  
  
<details>
  <summary>Aplicação</summary>
    <ul>
        <li><a href='src/app.py'>Código main da aplicação</a></li>
        <li><a href='src/insert.py'>Insert no banco de dados</a></li>
        <li><a href='src/schema.sql'>Schema</a></li>
        <li><a href='src/templates/'>Templates</a></li>
    </ul>
</details>

