import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get coordinates from the map
# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

# Reading the csv file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# using while loop to iterate over and ask the player to guess another state
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's the another state "
                                                                                        "name?").title()
    # Adding exit key and creating a file with missing states
    if answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
            new_states = pandas.DataFrame(missing_state)
            new_states.to_csv("states_to_learn.csv")
        break
    # Checking the state with the data in csv and adding it to their respective coordinates
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


