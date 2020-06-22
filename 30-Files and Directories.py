from pathlib import Path

# Absolute path
# E:\04-PROGRAMMING\Python

# path = Path("ecommerce")
# path = Path("ecommerce1")

# path = Path("emails")
# # print(path.mkdir())
# print(path.rmdir())
# print(path.exists())



path = Path()
# for file in path.glob('*.py'):    # Search a file using a pattern
for file in path.glob('*'):    # Searching all the files and directories in the current path
    print(file)


# Relative path
