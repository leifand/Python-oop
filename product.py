'''
    product.py
    Leif Anderson 7/8/17
'''

class Product(object):
    def __init__(self, price, name, weight, brand, cost, status='for sale'):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self, rate):
        return self.cost * (1 + rate)

    def returnProduct(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price * 0.8
        elif reason == 'like new':
            self.status = 'for sale'
        else:
            pass
        return self

    def displayinfo(self):
        print "Price  : " + str(self.price)
        print "name  : " + str(self.name)
        print "weight   : " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost    : " + str(self.cost)
        print "Status:" + str(self.status)
        return self

hamburger = Product(8.00, 'Ground Beef', 1.0, 'Kroger', 4.56, 'for sale')
cheese = Product(2.99, 'American Cheese', 1.0, 'Kraft', 1.03, 'for sale')
milk = Product(6.00, 'Whole Milk', 3.5, 'Bordens', 3.67, 'for sale')

hamburger.displayinfo()
print hamburger.addTax(0.0825)
hamburger.sell().displayinfo()
cheese.displayinfo().sell().displayinfo()
milk.displayinfo().sell().displayinfo()

hamburger.returnProduct('like new').displayinfo()
cheese.returnProduct('opened').displayinfo()
milk.returnProduct('defective').displayinfo()
