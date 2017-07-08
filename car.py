'''
    car.py
    Leif Anderson
'''

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayinfo()


    def displayinfo(self):
        print "Price  : " + str(self.price)
        print "Speed  : " + str(self.speed)
        print "Fuel   : " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax    : " + str(self.tax)
        return self

trabant = Car(1000, 25, 'empty', 16)
gremlin = Car(2000, 35, 'half tank', 19)
rabbit = Car(9000, 75, 'quarter tank', 28)
bmw = Car(12000, 125, 'full', 24)
porsche = Car(30000, 175, 'three quarters', 20)
ferrari = Car(75000, 225, 'full', 12)
