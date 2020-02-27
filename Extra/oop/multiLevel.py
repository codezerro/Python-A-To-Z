class MusicalInstruments:
    numberOfMajorKey=12


class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfString=6
        print("This Guiar has {} strings.It is made of {} and it can play {} keys".format(self.numberOfString,self.typeOfWood,self.numberOfMajorKey))


guitar = Guitar()