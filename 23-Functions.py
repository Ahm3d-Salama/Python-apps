""" Functions """
# def greet_user():
#     print("Hi there !")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user()
# print("Finish")


"""Parameters"""
# def greet_user(first_name):
#     print(f"Hi {first_name}!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user("John")
# greet_user("Mary")
# print("Finish")

"""parameter is a placeholder for the function to receiving information"""
"""Arguments is the actual information that supplied to these functions"""

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


# print("Start")
# greet_user("John", "Smith")
# print("Finish")

"""keyword Argument"""
# greet_user(last_name="Smith", first_name="John")
# greet_user(last_name="Smith", "John")               #positional args come first
#
#
# calc_cost(total = 50, shipping = 5, discount = 0.1)

"""Return Statment"""


# def square(number):
#     return number * number
#
#
# print(square(3))


def square(number):            # None is a default value for function
    print(number * number)


print(square(3))



"""Creating a Reusable Function"""



def emoji_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)": ":)",
        ":(": ":("
    }

    output = ""
    for word in words:
        output += emojis.get (word , word) + " "

    return output


msg = input(">")
print(emoji_converter(msg))





