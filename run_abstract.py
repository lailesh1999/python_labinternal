from abstract_module1 import example

class demo1(example):

    def area(self, g, h):
        return  g * h

    def volume(self,ac,bc):
        vol = ac * bc
        return  vol

d1 = demo1()
print(d1.area(20,30))
print(d1.volume(30,40))

