from application.models.dao.produtoDao import ProdutoDAO
from flask import render_template
from application import app

product_list = ProdutoDAO().listAll()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', product_list = product_list)

@app.route('/list', methods=['GET'])
def listaProduto():
    return render_template('produto_list.html', product_list = product_list)