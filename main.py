import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_sates = data.state.to_list()
states_guessed = []
game_is_on = True
cant_Guess = 0


while game_is_on:
    answer = screen.textinput(title=f"{cant_Guess}/50",
                              prompt="what's another state's name?").title()

    if answer == "Exit" or cant_Guess == 50:
        missing_states = [state for state in all_sates if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states__to_learn")
        break

    if answer in all_sates and answer not in states_guessed:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        loc = data[data.state == answer]
        t.goto(int(loc.x), int(loc.y))
        t.write(answer)
        cant_Guess += 1
        states_guessed.append(answer)


screen.exitonclick()