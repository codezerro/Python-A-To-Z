#public=> memberName
#protect=> _memberName
#private=> __memberName

class Car:
    numberOfWheels = 4 
    _color ="Black"

class Bmw(Car):
    def __init__(self):
        print("The protected class  color : {}".format(self._color))
car=Car()
print("Number of wheels in a car {}".format(car.numberOfWheels))
bmw=Bmw()