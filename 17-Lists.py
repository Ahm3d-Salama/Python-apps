# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names)

# print(names[0])
# print(names[2])
# print(names[-1])
# print(names[-2])
# print(names[2:])
# print(names[2:4])
#
# names[0] = 'Jon'
# print(names)

"""Write a program to find the largest number in a list"""
numbers = [2, 4, 5, 7, 9, 4, 1] # binary search
# temp = numbers[ 0 ]
# for number in numbers:
#     if number > temp:
#         temp = number
# print(temp)


"""Solution"""
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

"""Another Solution"""
numbers.sort()
numbers.reverse()
print(numbers[0])


