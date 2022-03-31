class myError(Exception):
    def __int__(self,value):
        self.value = value

class demo:

    def input(self):
        try:
            marks = int(input("ENTER THE MARKS"))

            if(marks < 0 or marks > 100):
                raise myError("INVALID MARKS PLEASE ENTER VALID ONE")
            else:
                print("MARKS HAVE BEEN ENTERED SUCESSFUILLY")

        except myError as e:
            print(e)
d1 = demo()
d1.input()