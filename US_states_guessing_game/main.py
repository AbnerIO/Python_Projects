import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
correct_guesses = []

# Pandas data
data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()

# The game
while scoreboard.points < len(states_list):
    answer_state = screen.textinput(title=f"{scoreboard.points}/50 States correct", prompt="What`s another state`s name?: ").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        scoreboard.add_point()
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        scoreboard.print_text(x, y, answer_state)
        correct_guesses.append(answer_state)

# Not guessed states (optional module)
for state_guess in correct_guesses:
    if state_guess in states_list:
        states_list.remove(state_guess)
print(states_list)
data_frame = pandas.DataFrame(states_list)
data_frame.to_csv("not_guessed.csv")


