import pandas
import turtle
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])
#
# dict_data = data.to_dict()
# # print(dict_data)
#
# temp_list = data['temp'].to_list()
# # print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # data in columns
# # print(data['condition'])
# # print(data.condition)
#
# # data in rows
# # print(data[data.day == 'Monday'])
# # print(data[data.temp == data["temp"].max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0] * 9 / 5 + 32
# # print(monday_temp)
#
# # Create DataFrame
# data_dicta = {
#   'students': ["Amy", "Oliver", "Danny"],
#   'scores': [76, 82, 55]
# }
#
# created_data = pandas.DataFrame(data_dicta)
# print(created_data)
# created_data.to_csv('created_data.csv')

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231204.csv")
# black = len(data[data["Primary Fur Color"] == "Black"])
# red = len(data[data["Primary Fur Color"] == "Cinnamon"])
# grey = len(data[data["Primary Fur Color"] == "Gray"])
#
# # for squirrel_color in data["Primary Fur Color"]:
# #     if squirrel_color == "Black":
# #         black += 1
# #     elif squirrel_color == "Cinnamon":
# #         cinnamon += 1
# #     elif squirrel_color == "Gray":
# #         gray += 1
# #     else:
# #         pass
#
# print(f"Black: {black}")
# print(f"Cinnamon: {red}")
# print(f"Gray: {grey}")
#
# squirrel_data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [grey, red, black],
# }
#
# squirrel_data = pandas.DataFrame(squirrel_data_dict)
# squirrel_data.to_csv("squirrel_count.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
correct_guesses = []
all_states = data.state.to_list()

while game_is_on:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="Guess the state:").title()

    if guess == "Exit":
        break
    if guess in data.state.to_list():
        guessed_state = data[data['state'] == guess]
        # print(guessed_state)
        state_x = int(guessed_state.x.iloc[0])
        state_y = int(guessed_state.y.iloc[0])
        # print(state_x, state_y)

        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(state_x, state_y)
        state_turtle.write(guess)

        score += 1
        all_states.remove(guess)
        correct_guesses.append(guess)

states_to_learn = {
    "States To Learn": all_states,
}

states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")
