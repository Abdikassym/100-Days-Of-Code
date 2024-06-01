n = [1, 2, 3, 4, 5, 6]
new_n = [i + 1 for i in n]

name = "Abdesha"
letters = [n for n in name]

doubled_nums = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) == 4]
cap_long_names = [name.upper() for name in names if len(name) > 4]
print(cap_long_names)
