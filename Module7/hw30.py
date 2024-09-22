import os

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        else:
            return ''

    def add(self, *products):
        existing_products = self.get_products().splitlines()

        with open(self.__file_name, 'a') as file:
            for product in products:
                if str(product) not in existing_products:
                    file.write(str(product) + '\n')
                else:
                    print(f"Продукт {product} уже есть в магазине")

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
