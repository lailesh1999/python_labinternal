class distance:
    def __init__(self,inches,feet):
        self.inches = inches
        self.feet = feet
    def cal(self):
        if self.inches >= 12:
            self.feet = self.feet + 1
            self.inches = self.inches - 1

    def display(self):
        print(self.inches,"\t\t\t ",self.feet)


num = int(input("HOW MANY DISTNACE OBJECT NEED TO BE INSERTED"))
ele =[]
for i in range(0,num):
    feet = int(input("ENTER THE FEET:"))
    inches = int(input("ENTER THE INCHES:"))
    d1 = distance(feet,inches)
    ele.append(d1)
print("================================")
print("FEET \t\t INCHES")
print("================================")
for row in ele:
    row.cal()
    row.display()
