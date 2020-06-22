# weight = input('What is your weight? ')
# unit = input("(L)bs or (K)g: ")
#
# if unit == "k" or "K":
#     weight_kgs = round(float(weight) / 0.45, 2)
# print('Your are ' + str(weight_kgs) + ' Kgs')
#
# else unit = "l" and "L":
#     weight_lbs = round (float (weight) * 0.45, 2)
# print('Your weight is = ' + str(weight_lbs) + ' Kgs')
#

weight = float(input('What is your weight? '))
unit = input("(L)bs or (K)g: ")


if unit.upper() == "L":
    converted = round(weight * 0.45, 2)
    print(f'Your weight is {converted} Kgs')
else:
    converted = round(weight / 0.45, 2)
    print(f'Your are {converted}  lbs')




