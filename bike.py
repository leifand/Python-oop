'''
    bike.py
    Leif Anderson 7/8/17
'''

class Bike(object):
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.totalMiles = 0

    def displayinfo(self):
        print "Price    : " + str(self.price)
        print "Max Speed: " + str(self.maxSpeed)
        print "Miles    : " + str(self.totalMiles)
        return self

    def ride(self):
        print "Riding ..."
        self.totalMiles += 10
        return self

    def reverse(self):
        print "Reversing ..."
        self.totalMiles -= 5
        return self

ninja = Bike(15000, 240)
harley = Bike(13500, 160)
tricycle = Bike(15, 5)

ninja.displayinfo().ride().displayinfo().ride().displayinfo()
print '>>>>>>>>>>>'
tricycle.displayinfo().reverse().displayinfo().reverse().displayinfo()
