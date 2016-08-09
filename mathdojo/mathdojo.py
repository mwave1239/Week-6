#Part 1
class MathDojo(object):
    def __init__(self):
        self.sum = 0
        self.sub = 0
    def add(self, *restOfArg):
        for arg in restOfArg:
            self.sum = self.sum + arg
        return self
    def subtract(self, *restOfArg):
        for arg in restOfArg:
            self.sub = self.sub + arg
        return self
    def result(self):
        print (self.sum - self.sub)

MathDojo().add(2).add(2, 5).subtract(3, 2).result()

#Part Deaux and 3. I just added the tuple check
class MathDojo2(object):
    def __init__(self):
        self.sum = 0
        self.sub = 0
    def add(self, *restOfArg):
        for arg in restOfArg:
            if type(arg) == list:
                for x in arg:
                    self.sum = self.sum + x
            elif type(arg) == tuple:
                for x in arg:
                    self.sum = self.sum + x
            else:
                self.sum = self.sum + arg
        return self
    def subtract(self, *restOfArg):
        for arg1 in restOfArg:
            if type(arg1) == list:
                for y in arg1:
                    self.sub = self.sub + y
            elif type(arg1) == tuple:
                for x in arg1:
                    self.sum = self.sum + x
            else:
                self.sub = self.sub + arg1
        return self

    def result(self):
        print (self.sum - self.sub)

MathDojo2().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
