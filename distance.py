class distance:
    def __init__(self, f, i):
        self.f = f
        self.i = i

    def input(self):
        self.f = int(input("ENTER THE FEET"))
        self.i = int(input("ENTER THE INCHES"))

    def display(self):
        print("FEEE:",self.f,"INCHES:" ,self.i)

    def __add__(self, other):
        feet = self.f + other.f
        inch = self.i + other.i

        return distance(feet, inch)


d1 = distance(2, 4)
d2 = distance(5, 6)

d1.input()
d2.input()

d3 = d1 + d2
d3.display()
