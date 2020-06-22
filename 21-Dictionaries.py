customer = {
    "first_name": "John Smith",
    "age": 30,
    "email": "John.Smith@user.com",
    "is_verified": True
}

# print(customer[ "first_name"])

# print(customer[ "Name"])

# print(customer[ "birthdate"])

# print(customer.get("birthdate"))

# print(customer.get("birthdate", "Jan 11"))
#
# customer["first_name"] = "Jack smith"

# print(customer["first_name"])


""" Convert the phone digits to strings """
phone = input("Phone: ")

digits_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three"
}

output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!") + " "
print(output)



