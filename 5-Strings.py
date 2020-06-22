# course = "Python's course for Beginners"

# print(course[0])
# print(course[-1])
# print(course[-2])
# print(course[0:3])
# print(course[0:])
# print(course[1:])
# print(course[:5])
# print(course[:])    # copy string
#
# another = course[:]
# print(another)

#######################################
# first_name = 'Jennifer'
# print(first_name[1:-1])

#######################################
# Formatted Strings
# first = 'john'
# last = 'Smith'
# john [smith] is a coder
# message = first + ' [' + last + '] ' + 'is a coder'
#
# print(message)
#
# msg = f'{first} [{last}] is a coder'
#
# print(msg)

#######################################
# string Methods
course = "Python's course for Beginners"

# print(len(course))  # count number of chars
# print(course.upper())
# print(course.lower())

print(course.find('p'))  # prints -1 means not exist
print(course.find('P'))
print(course.find('o'))

print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))

print('Python' in course)

print(course.title())  # to capitalize the first letter of every word







