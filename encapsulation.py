


#Protected variable

class Dog:
    def __init__(self):
        self._protectedVar=0

obj=Dog()
obj._protectedVar=43
print(obj._protectedVar)


#Private Attribute

class Protected:
    def __init__(self):
        self._private =9

    def getPrivate(self):
        print(self._private)

    def setPrivate(self, private):
        self._privateVar = private

obj =Protected()
obj.getPrivate()
obj.setPrivate(23)

    
