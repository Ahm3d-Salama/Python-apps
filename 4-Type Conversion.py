# birth_year = input('Birth year: ')
#
# age = 2020 - int(birth_year)  # convert the string value
#
# print('You are ' + str(age) + ' years')

# Ask user their weight (in pounds), convert it to kilograms and print on terminal

weight_pounds = input('What is your weight in pounds?')

weight_kilograms = round(float(weight_pounds), 2)  * 0.45

print('Your weight is = ' + str(weight_kilograms) + ' Kgs')