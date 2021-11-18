from application.models.entity.produto import Produto
import json
from typing import List

class ProdutoDAO():
    def listAll(self) -> List[Produto]:
        result = []
        with open('products.json', 'r') as file:
            produto_list = json.load(file)
            result = self.dict_to_list(produto_list)
        return result

    def dict_to_list(self, produto_dict):
        resultado = []

        for produto in produto_dict:
            produtoL = Produto()
            produtoL.setId(produto['id'])
            produtoL.setName(produto['name'])
            produtoL.setImage(produto['image'])
            produtoL.setOldPrice(produto['oldPrice'])
            produtoL.setPrice(produto['price'])
            produtoL.setDescription(produto['description'])
            produtoL.setCount(produto['installments']['count'])
            produtoL.setValue(produto['installments']['value'])
            resultado.append(produtoL)
        return resultado