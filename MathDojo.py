'''
    MathDojo.py
    Leif Anderson 7/9/17
'''

class MathDojo(object):

    def __init__(self):
        self.sum = 0

    def reset(self):
        self.sum = 0
        return self

    def add(self, n):
        if isinstance(n, int):
            self.sum += n
        elif isinstance(n, list):
            for i in range(0,len(n)):
                self.sum += n[i]
        elif isinstance(n, tuple):
            pass
        return self

    def subtract(self, n):
        if isinstance(n, int):
            self.sum -= n
        return self

    def result(self):
        print self.sum
        return self

a = MathDojo()

a.add(5).add(5).result().subtract(3).result().reset().result()
a.add([4,5,6]).result()
