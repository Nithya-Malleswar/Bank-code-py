"""
 
single inheritance:-


class restaurant():
    def waiter(self):
        print("Take order for customers")
class hotel(restaurant):
    def waiter1(self):
        print("Give me menu")
obj=hotel()
obj.waiter()
obj.waiter1()
 
 

multiple inheritance:-


class cat():
    def pilli(self):
        print("Meow Meow")
class dog():
    def kukka(self):
        print("Bow Bow")
class crow(cat,dog):
    def kaki(self):
        print("Kaww kaww")
obj=crow()
obj.pilli()
obj.kukka()
obj.kaki()



Multi-level inheritance:-



class karnataka():
    def state(self):
        print('karnataka is a state')
class bangalore(karnataka):
    def city(self):
        print("Bangalore is a city")
class marathahalli(bangalore):
    def area(self):
        print("Marathahalli is a area")
obj=marathahalli()
obj.state()
obj.city()
obj.area()



Hierarchical inheritance:-



class parent():
    def father(self):
        print("I am father")
class child1(parent):
    def son(self):
        print("I am big son")
class child2(parent):
    def son1(self):
        print("I am small son")
obj=child1()
obj.father()
obj.son()

obj=child2()
obj.father()
obj.son1()



Hydrid inheritance:-



class Nithya():
    def man(self):
        print("I'm from madhavaram")
class prasad(Nithya):
    def man1(self):
        print("I'm from kotha madhavaram")
class madhu():
    def man2(self):
        print("I'm from nekanapuram")
class malleswar(prasad,madhu):
    def man3(self):
        print("I'm from mrukundasram")
obj=malleswar()
obj.man()
obj.man1()  
obj.man2()
obj.man3()

"""

#classes and objects

# class Bike:
#     def __init__(self,Company,Model,Miliege,speed):
#         self.Company=Company
#         self.Model=Model
#         self.Miliege=Miliege
#         self.Speed=speed
# Bike1=Bike("Pulsar",2019,35,150)
# print(Bike1.Company)
# print(Bike1.Model)
# print(Bike1.Miliege)
# print(Bike1.Speed)



class A:
    def fun(self):
        print("It is a A")
class B:
    def fun(self):
        print("It is a B")
class C:
    def fun(self):
        print("It is a C")
def poly(obj):
    obj.fun()

obj1=A()
obj2=B()
obj3=C()

poly(obj1)
poly(obj2)
poly(obj3)