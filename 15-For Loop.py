# for item in "Python":
#     print(item)


# for item in ["Mosh", "John", "Sarah"]:
#     print(item)

# for item in [1, 2, 3, 4]:
#     print(item)

# for item in range(10):
#     print(item)


# for item in range(5, 10, 2):
#     print(item)

"""
write a program to calculate all shopping item in shopping cart
"""
prices = [10, 20, 30]

for price in prices:
    print(f"Total: {sum(prices)}")
    break


prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")