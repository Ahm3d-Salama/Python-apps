"""Dry"""
class Mammel:
    def walk(self):
        print ("walk")


class Dog(Mammel):
    def bark(self):
        print("Bark")


class Cat(Mammel):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()

# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")

