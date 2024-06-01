# loops lesson
students_heights = input("Input heights by separating them with 'space': ").split()

total_height = 0
number_of_students = 0
average_height = 0

for student_height in students_heights:
    total_height += int(student_height)
    number_of_students += 1

    average_height = total_height // number_of_students

print("Total height is", total_height)
print("Total number of students is", number_of_students)
print("Average height is", average_height)



















