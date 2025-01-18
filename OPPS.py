#single inheritance

# class parent():
#     def father(self):
#         print("I am a father")
# class child(parent):
#     def child1(self):
#         print("I am a child")
# obj=child()
# obj.father()
# obj.child1()

#----------------------------------------------

#multiple inheritance

# class dog():
#     def bow(self):
#         print("Bow Bow")
# class cat():
#     def meow(self):
#         print("meow meow")
# class rat(dog,cat):
#     def mouse(self):
#         print("Rat Rat")
# obj=rat()
# obj.bow()
# obj.meow()
# obj.mouse()

#------------------------------------------------------

#multi-level inheritance

# class dog():
#     def bow(self):
#         print("Bow Bow")
# class cat(dog):
#     def meow(self):
#         print("meow meow")
# class rat(cat):
#     def mouse(self):
#         print("Rat Rat")
# obj=rat()
# obj.bow()
# obj.meow()
# obj.mouse()


#-----------------------------------------------------

#Hierarchical inheritance:-

class dog():
    def bow(self):
        print("Bow Bow")
class cat(dog):
    def meow(self):
        print("meow meow")
class rat(dog):
    def mouse(self):
        print("Rat Rat")
# obj=rat()
# obj.mouse()
# obj.bow()

obj=cat()
obj.meow()
obj.bow()