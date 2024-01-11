import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 78, 92]
# }
#
# students_df = pandas.DataFrame(student_dict)

# for (key, value) in students_df.items():
#     print(value)

# Loop through rows of data frame
# for (index, row) in students_df.iterrows():
#     if row.student == "Lily":
#         print(row.score)



data = pandas.read_csv("nato_phonetic_alphabet.csv")


def nato_alphabet():
    word = input("Enter a word: ")
    data_dict = {row.letter: row.code for index, row in data.iterrows()}
    nato_code = [data_dict[i] for i in word.upper()]
    print(nato_code)


try:
    nato_alphabet()
except KeyError:
    print("Sorry, only english alphabet letters allowed. Please, try again.")
    nato_alphabet()
