'''
    store.py
    Leif Anderson
'''
from product import Product

class Store(object):
    def __init__(self, location, owner, products=[]):
        self.products = products
        self.location = location
        self.owner = owner

    def addProduct(self, newProduct):
        self.products.append(newProduct)
        return self

    def removeProduct(self, product2Remove):
        for prod in self.products:
            if prod == product2Remove:
                self.products.remove(prod)
        return self

    def inventory(self):
        listLen = len(self.products)
        for i in range(0, listLen):
            self.products[i].displayinfo()
        return self

hamburger = Product(8.00, 'Ground Beef', 1.0, 'Kroger', 4.56, 'for sale')
cheese = Product(2.99, 'American Cheese', 1.0, 'Kraft', 1.03, 'for sale')
milk = Product(6.00, 'Whole Milk', 3.5, 'Bordens', 3.67, 'for sale')

myStore = Store('Dallas, Texas', 'Leif Anderson')
myStore.addProduct(hamburger).addProduct(cheese).addProduct(milk).inventory()
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
myStore.removeProduct(cheese).inventory()
