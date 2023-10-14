class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{item.name}: {item.price}' for item in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Sony', 15000))
cart.add(TV('Samsung', 20000))
cart.add(Table('Ореховый', 10000))
cart.add(Notebook('Lenovo', 40000))
cart.add(Notebook('Asus', 35000))
cart.add(Cup('Смешная', 200))
