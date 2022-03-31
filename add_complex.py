class add_complex:
    def input(self):
        self.real = int(input("ENTER THE REAL PART"))
        self.image= int(input("ENTER THE IMAGINARY PART"))

    def display(self):
        print(f"{self.real}")
        print(f"{self.image}")

    def __add__(self, other):
        r = self.real + other.real
        i = self.image + other.image
        return r ,i


a1 = add_complex()
a1.input()
a1.display()

a2 = add_complex()
a2.input()
a2.display()


print(a1 + a2)
