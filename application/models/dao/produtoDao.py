from application.entity.produto import Produto
import json
from typing import List

class ProdutoDAO:
    def listAll(self) -> List[Produto]:
        result = []
        with open('products.json', 'r') as file:
            produto_dict_list = json.load(file)
            for produto_dict in produto_dict_list:
                id = produto_dict.get("id", None)
                name = produto_dict.get("name", None)
                image = produto_dict.get("image", None)
                oldPrice = produto_dict.get("oldPrice", None)
                price = produto_dict.get("price", None)
                descricao = produto_dict.get("descricao", None)
                count = produto_dict.get("count", None)
                value = produto_dict.get("value", None)
                product = Produto(id, name, image, oldPrice, price, descricao, count, value)
                result.append(product)
        return result