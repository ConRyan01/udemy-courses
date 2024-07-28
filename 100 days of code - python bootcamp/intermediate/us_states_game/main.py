import turtle
import pandas

PATH = "C:\\Users\\mwysz\\OneDrive\\Documents\\Github\\Python-3\\Udemy Courses\\100 days of code - python bootcamp\\intermediate\\us_states_game"


screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{PATH}\\blank_states_img.gif"
screen.addshape(image)
screen.setup(750, 500)
turtle.shape(image)
file_data = pandas.read_csv(f"{PATH}\\50_states.csv")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
all_states = file_data.state.to_list()
guesses = []

def write_state(answer):
    current_row = file_data[file_data.state == answer]
    writer.goto(current_row.x.item(), current_row.y.item())
    writer.write(current_row.state.item())


while len(guesses) < 50:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 Correct", prompt="Enter a State's name").title()

    if answer_state in file_data.state.values and answer_state not in guesses:
        write_state(answer_state)
        guesses.append(answer_state)

    elif answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f'{PATH}\\states_to_learn.csv')
        break

