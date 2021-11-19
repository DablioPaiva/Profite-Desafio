class Product:
    def __init__(self, id1, name, image, price, price1, description, count, value) -> object:
        """

        :param id1:
        :param name:
        :param image:
        :param price:
        :param price1:
        :param description:
        :param count:
        :param value:
        :rtype: object
        """
        self.__id = None
        self.__name = None
        self.__image = None
        self.__oldPrice = None
        self.__price = None
        self.__description = None
        self.__count = None
        self.__value = None

    def setId(self, id: int):
        self.__id = id

    def setName(self, name: str):
        self.__name = name

    def setImage(self, img: str):
        self.__image = img

    def setOldPrice(self, oldPrice: int):
        self.__oldPrice = oldPrice

    def setPrice(self, price: int):
        self.__price = price

    def setDescription(self, description: str):
        self.__description = description

    def setCount(self, count: int):
        self.__count = count

    def setValue(self, value: float):
        self.__value = value

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getImage(self):
        return self.__image

    def getOldPrice(self):
        return self.__oldPrice

    def getPrice(self):
        return self.__price

    def getDescription(self):
        return self.__description

    def getCount(self):
        return self.__count

    def getValue(self):
        return self.__value

    def toDict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "image": self.__image,
            "oldPrice": self.__oldPrice,
            "price": self.__price,
            "description": self.__description,
            "installments": {
                "count": self.__count,
                "value": self.__value
            }
        }