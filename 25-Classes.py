class Point:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)


"""Constructor is an function that's called at the time of creating an object"""
# point2 = Point()
# print(point2.x)

# point = Point(10, 20)
# point.x = 11
# print(point.x)

"""
person 
    - name
    - talk()
"""

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, ):
        print(f"Hi, Iam {self.name} ")


John = Person("John Smith")
# print(John.name)
John.talk()

Bob = Person("Bob Smith")
Bob.talk()