from application.models.entity.produto import Product
import json
from typing import List


class ProdutoDAO():
    def listAll(self) -> List[Product]:
        result = []
        with open('products.json', 'r') as file:
            product_dict_list = json.load(file)

            for product_dict in product_dict_list:
                id = product_dict.get("id")
                name = product_dict.get("name")
                image = product_dict.get("image", None)
                oldPrice = product_dict.get("oldPrice", None)
                price = product_dict.get("price", None)
                description = product_dict.get("description", None)
                count = product_dict.get("count", None)
                value = product_dict.get("value", None)
                product = Product(id, name, image, oldPrice, price, description, count, value)
                result.append(product)
        return result
