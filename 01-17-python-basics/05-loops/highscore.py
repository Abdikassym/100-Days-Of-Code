student_scores = input().split()

highest_score = 0
for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)
        print(f"{score} is now the highest score")
    else:
        print(f"{score} in not higher than {highest_score}")

print(highest_score)


