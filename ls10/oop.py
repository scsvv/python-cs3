class Car: 

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    
    def engien_on(self):
        print( f"{self.name} is on")


bmw = Car("X7", "BMW")
print(bmw.mark)
bmw.engien_on()

audi = Car("R", "Audi")
print(audi.mark)
audi.engien_on()