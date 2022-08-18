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

    produtos_lista = ['mesa', 'cadeira', 'papel', 'caneta']

    return render_template('produtos.html', produtos=produtos_lista)

@app.route("/produto/<nome_produto>")
def produto(nome_produto):

    produto_dict = {
        'cadeira': {
            'nome': 'cadeira de escritorio',
            'descricao': 'Essa cadeira é excelente',
            'cor': 'vermelha',
            'valor': 'R$ 10,50'
        },
        'mesa': {
            'nome': 'mesa de escritorio',
            'descricao': 'mesa boa para trabalhar',
            'cor': 'azul',
            'valor': 'R$ 50,00'
        },
        'papel': {
            'nome': 'papel 4x4',
            'descricao': 'papel para desenhar',
            'cor': 'branca',
            'valor': 'R$ 2,99'
        },
        'caneta': {
            'nome': 'Caneta BIC',
            'descricao': 'Caneta muito boa',
            'cor': 'azul',
            'valor': 'R$ 1,00'
        },
    }


    # produto_list = ['branco', 'R$ 10,50']

    return render_template(
        'produto.html',
        produto = produto_dict[nome_produto]
    )

@app.route('/usuario/<nome_usuario>')
def usuario(nome_usuario):

    usuarios = ['gabriela', 'enzo', 'larissa', 'lucas', 'donizete', 'danton']

    if nome_usuario in usuarios:
        return render_template('usuario.html', usuario=nome_usuario)
    else:
       return render_template('usuario.html', usuario=None) 
   