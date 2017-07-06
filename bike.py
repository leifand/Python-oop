'''
    bike.py
    Leif Anderson 7/6/17
'''

class Bike(object):
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.totalMiles = 0

    def displayinfo():
        print "Price    : " + str(price)
        print "Max Speed: " + str(maxSpeed)
        print "Miles    : " + str(totalMiles)
        return self

    def ride():
        print "Riding ..."
        totalMiles += 10
        return self

    def reverse():
        print "Reversing ..."
        totalMiles -= 5
        return self

ninja = Bike(15000, 240)
harley = Bike(13500, 160)
tricycle = Bike(15, 5)

ninja.displayinfo()
