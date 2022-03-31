class person:
    def __init__(self,name = None,age = None):
        self.name = name
        self.age = age

    def input(self):
        self.name = input("ENTER NAME")
        self.age = input("AGE")
    def display(self):
        print(f"NAME OF PERSON {self.name}")
        print(f"AGE OF PERSON{self.age}")

class student(person):
    def __init__(self,name=None,age=None,course=None,reg=None):
        super().__init__(name,age)
        self.course = course
        self.reg = reg

    def input(self):
        super().input()
        self.course = input("ENTER THE COURSE")
        self.reg =  input("ENTER THE REG NO")

    def display(self):
        super().display()
        print(f"course {self.course}")
        print(f"REG NO{self.reg}")

s1 = student()
s1.input()
s1.display()

s2 = student("veugas",34,'ddf',2222)
#s2.input()
s2.display()



