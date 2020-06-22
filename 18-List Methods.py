# numbers = [5, 2, 1, 7, 4]

# numbers.append(13)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.clear()

# numbers.pop()
# numbers.reverse()
# numbers.sort()
# numbers.extend([8, 9, 15])

# print(numbers.index(2))
# print(50 in numbers)
#
# print(numbers.count(5))

# numbers_2 = numbers.copy()
# numbers.append(10)
# print(numbers_2)

""" Write a program to remove the duplicates in a list """
numbers_3 =[1, 1, 3, 8, 7, 3, 2, 8]
# diplicate = [0]
#
# for item in numbers_3:
#     if diplicate == item in numbers_3:
#         numbers_3.remove(diplicate)
#     print(numbers_3)

"""Solution"""

uniques = []
for number in numbers_3:
    if number not in uniques:
        uniques.append(number)
print(uniques)