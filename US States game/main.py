import turtle
import pandas
from answer import Answer
answer = Answer()
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data[data["state"] == "Ohio"])
# a = list(data[data["state"] == "Ohio"])
# print(a)

all_states = data.state.to_list() #A way to turn the values of a colum to a list
#--------------------------------------------------------------------------------
all_Xs = data.x.to_list()
all_Ys = data.y.to_list()
print(all_states)
print(all_Xs)
print(all_Ys)

linha = data.iloc[0].to_list() #A way to turn the line of a DF to a List
print(int(linha[1])) #And turn the value to a int
#--------------------------------------------------------------------------------

game_is_on = True
score = 0
correct_guesses = []

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()
    x = data[data["state"] == answer_state]
    y = data[data["state"] == answer_state]
    ans_x = x["x"].tolist()
    ans_y = y["y"].tolist()

    if answer_state == "Exit":
        # Create a .csv with the missing states to learn:
        for state in correct_guesses:
            all_states.remove(state)

        df = pandas.DataFrame(all_states, columns=['States to learn'])
        df.to_csv('States_to_learn.csv', index=False)  # This index= false exclude the colum with the item numbers
        print(len(all_states))

        # states_to_learn = [all_states.remove(states) for states in correct_guesses]
        # print(correct_guesses)
        # print(states_to_learn)
        # print(len(states_to_learn))

        break


    exist = data["state"].isin([answer_state]).any()
    if exist:
        answer.check_answer(answer_state, int(ans_x[0]), int(ans_y[0]))
        score += 1
        correct_guesses.append(answer_state)

    if len(correct_guesses) == 50:
        print("You win!")
        game_is_on = False











































# screen.exitonclick()