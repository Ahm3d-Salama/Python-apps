'''
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold

'''

# temperature = 20
#
# if temperature >= 30:
#     print("it's a hot day")
# elif temperature <= 10:
#     print("it's a cold day")
# else:
#     print("it's neither hot nor cold")

"""
if first_name is less than 3 characters long
    first_name must be at least 3 characters
otherwise if it's more than 50 characters long
    first_name can be a maximum of 50 characters
otherwise
    first_name looks good
    
"""
# characters = int(input("Enter first_name characters: "))
# if characters <= 3:
#     print("first_name must be at least 3 characters")
# elif characters >= 50:
#     print("first_name can be a maximum of 50 characters")
# else:
#     print("first_name looks good")


name = "Ahm"
if len(name) <= 3:
    print("first_name must be at least 3 characters")
elif len(name) >= 50:
    print("first_name can be a maximum of 50 characters")
else:
    print("first_name looks good")



