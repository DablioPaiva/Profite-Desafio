from application import app
from flask import render_template
from application.models.dao.produtoDao import ProdutoDAO

produto_list = ProdutoDAO().listAll()

@app.route('/list', methods=['GET'])
def index():
    return render_template('index.html', produto_list=produto_list)

