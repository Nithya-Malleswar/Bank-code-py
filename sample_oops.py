class item():
    def food(self):
        print("item name chicken")
class item1(item):
    def dinner(self):
        print("item name pizza")
        
obj=item1()
obj.food()
obj.dinner()

class Dog():
    def speak(self):
        print("Bow Bow")
class cat(Dog):
    def meow(self):
        print("pilli")
obj=cat()
obj.speak()
obj.meow()



 



# class Animal():
#     def eat(self):
#         print("It is a animal")
# class Bird(Animal):
#     def fly(self):
#         print("It is a bird")
# class car():
#     def things(self):
#         print("It is a car")
# class bus(Bird,car):
#     def engine(self):
#         print("It ia a bus")
# obj=bus()
# obj.eat()
# obj.fly()
# obj.things()
# obj.engine()

