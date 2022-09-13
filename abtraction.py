from abc import ABC, abstractmethod
class Animal(ABC):
    def paySlip(self, amount):
        print("Dogs bought:",amount)

        @abstractmethod
        def payment(self,amount):
            pass

class Dogs(Animal):
    def payment(self,amount):
        print('Your total amount of dogs purchased, {}, exceed the number of dogs in local stores\nPlease try again at a later time'.format(amount))

obj = Dogs()
obj.paySlip("349249021")
obj.payment("349249021")
