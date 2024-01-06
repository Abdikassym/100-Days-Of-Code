# try:
#     with open("doc.txt") as file:
#         print(f"{file.read()} company")
# except FileNotFoundError:
#     print(f"There is no File. Creating file...")
#     with open("doc.txt", "a") as file:
#         file.write("Something")
#         print("File created and filled with data")
# else:
#     print("File read completely")
# finally:
#     raise KeyError("I can create my own errors also")


# try:
#     dictionary = {
#         'key': 'value'
#     }
#     print(dictionary['new_key'])
# except KeyError as error_key:  # I can return the values that create an exception
#     print(f"{error_key} does not exist")

# Why do I need to raise me own exceptions?
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shall not exceed 3 meters.")
if weight > 200:
    raise ValueError("Human weight shall not exceed 200 kilogramms.")
print(f"BMI: {weight / height ** 2}")
