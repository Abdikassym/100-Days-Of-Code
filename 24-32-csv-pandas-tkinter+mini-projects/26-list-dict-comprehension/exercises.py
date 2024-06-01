# # square all the numbers with list comprehension
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)
#
#
# # filter even numbers 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 - input
# list_of_strings = input().split(',')
# list_of_even_numbers = [int(num) for num in list_of_strings if int(num) % 2 == 0]
# print(list_of_even_numbers)


with open("file1.txt") as file:
    list1 = [int(num.strip("\n")) for num in file]
with open("file2.txt") as file:
    list2 = [int(num.strip("\n")) for num in file]

list3 = [num for num in list1 if num in list2]
print(list3)



