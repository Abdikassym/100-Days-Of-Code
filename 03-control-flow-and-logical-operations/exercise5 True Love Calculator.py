first_name = input("Enter your name: ").lower()
second_name = input("Enter your partner's name: ").lower()
full_name = first_name + second_name

first_count = 0
first_count += full_name.count("t")
first_count += full_name.count("r")
first_count += full_name.count("u")
first_count += full_name.count("e")

second_count = 0
second_count += full_name.count("l")
second_count += full_name.count("o")
second_count += full_name.count("v")
second_count += full_name.count("e")

score = str(first_count) + str(second_count)
print(score)








