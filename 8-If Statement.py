# is_hot = False
# is_cold = False
#
# if is_hot:
#  print('hot day')
# elif is_cold:
#  print('cold day')
# else:
#  print('beautiful day')

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
#
# elif is_cold:
#     print("It's a cold day")
#     print("Wear Warm clothes")
#
# else:
#     print("It's a lovely day")
#
# print("Enjoy you day")

#######################################
'''Price of a house is $1M
if buyer has good credit,
       they need to put down 10%
    otherwise
        they need to put down 20%
    print down payment    
    
'''
# price = 1000000
# good_credit = False
#
# if good_credit:
#
#     down_payment = float(price) * 0.1
# else:
#     down_payment = float (price) * 0.2
#
# # print("down payment = " + str(down_payment))
# print(f'Down payment = ${down_payment}')
#######################################
grade = float(input('What is yor grade?'))

if 85 < grade < 100:
    print('Excellent')
elif 75 < grade < 85:
    print('Very Good')
elif 65 < grade < 75:
    print('Good')
elif 50 < grade < 65:
    print('Pass')
else:
    print('Fail')
