from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def conectar_banco():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/")
def index():
    return render_template("index.html")


# AUTORES
@app.route("/autores")
def autores():

    conexao = conectar_banco()

    autores = conexao.execute(
        "SELECT * FROM autores"
    ).fetchall()

    conexao.close()

    return render_template(
        "autores.html",
        autores=autores
    )

# LIVROS
@app.route("/livros")
def livros():

    conexao = conectar_banco()

    livros = conexao.execute("""
        SELECT 
            livros.id_livro,
            livros.titulo,
            livros.ano,
            autores.nome AS autor
        FROM livros
        LEFT JOIN autores
        ON livros.id_autor = autores.id_autor
    """).fetchall()

    autores = conexao.execute(
        "SELECT * FROM autores"
    ).fetchall()

    conexao.close()

    return render_template(
        "livros.html",
        livros=livros,
        autores=autores
    )
# LEITORES
@app.route("/leitores")
def leitores():

    conexao = conectar_banco()

    leitores = conexao.execute(
        "SELECT * FROM leitores"
    ).fetchall()

    conexao.close()

    return render_template(
        "leitores.html",
        leitores=leitores
    )



if __name__ == "__main__":
    app.run(debug=True)