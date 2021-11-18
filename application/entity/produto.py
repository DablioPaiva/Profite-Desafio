class Produto:
    def __init__(self, id: int, name: str, image: str, oldPrice: int, price: int, description: str, count: int,
                 value: float):
        self._id = id
        self._name = name
        self._image = image
        self._oldPrice = oldPrice
        self._price = price
        self._description = description
        self._count = count
        self._value = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def oldPrice(self):
        return self._oldPrice

    @oldPrice.setter
    def oldPrice(self, value):
        self._oldPrice = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def toDict(self):
        return {
            "id": self._id,
            "name": self._name,
            "image": self._image,
            "oldPrice": self._oldPrice,
            "price": self._price,
            "description": self._description,
            "count": self._count,
            "value": self._value
        }
