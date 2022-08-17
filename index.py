from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <h1>Loja virtual</h1>
        <p>Compre seus produtos, pelo melhor preço </p>

        <a href="/produtos">Nosso Produtos</a>
    """

@app.route('/produtos/')
def produtos():
    return render_template('produtos.html')

# @app.route("/produtos")
# def produtos():
#     return """
#         <h2>Cadeira</h2>
#         <p>R$ 10,00</p>
#         <a href="/produto/Cadeira">Ver mais</a>

#         <h2>Mesa</h2>
#         <p>R$ 10,50</p>
#         <a href="/produto/Mesa">Ver mais</a>

#         <h2>Papel</h2>
#         <p>R$ 11,50</p>
#         <a href="/produto/Papel">Ver mais</a>

#         <br><br>
#         <a href="/">Voltar</a>
#     """

@app.route("/produto/<nome_produto>")
def produto(nome_produto):

    produtos = {
        'Cadeira': 'caderia preta',
        'Mesa': 'Essa mesa é muito legal',
        'Papel': 'Este papel é branco'
    }
    return render_template('produto.html', nome_produto = nome_produto)