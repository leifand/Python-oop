'''
    animal.py
    Leif Anderson 7/8/17
'''

class Animal(object):
    def __init__(self, name, health=0):
        self.name = name
        self.health = health

    def displayhealth(self):
        print "Health :" + str(self.health)
        return self

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print 'I am a Dragon!'
        return self

a = Animal('horse', 150)
b = Dog('Fido')
c = Dragon('Smaug')

a.run().run().walk().walk().displayhealth()
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
b.walk().walk().walk().run().run().pet().displayhealth()
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
c.fly().fly().fly().displayhealth()
