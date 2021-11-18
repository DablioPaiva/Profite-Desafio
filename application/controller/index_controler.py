from application.models.dao.produtoDao import ProdutoDAO
from flask import render_template
from application import app



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list')
def listAll():
    list_produto = ProdutoDAO().listAll()
    return render_template("produto_list.html",list_produto=list_produto)