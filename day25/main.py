# Main

import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game by blurridge")
us_map_image = "./blank_states_img.gif"
screen.addshape(us_map_image)
turtle.shape(us_map_image)

us_data_csv = "./50_states.csv"
data = pd.read_csv(us_data_csv)

correct = 0
correct_guesses = list()
to_study = list()

continue_game = True 

while continue_game:
    answer = screen.textinput(title=f"Guess the state {correct}/50", prompt="Type in the name of a state:").title()

    if answer == "Exit":
        for state in data["state"].values:
            if state not in correct_guesses:
                to_study.append(state)
        df = pd.DataFrame(to_study, columns=["To Study"])
        df.to_csv("./to_study.csv")
        continue_game = False 

    if answer in data["state"].values and answer not in correct_guesses:
        correct_guesses.append(answer)
        correct += 1
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        x = int(data[data.state == answer].x)
        y = int(data[data.state == answer].y)
        new_state.setpos(x, y)
        new_state.write(answer, font=("Helvetica", 12, "normal"))

    if correct == 50:
        continue_game = False 
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.setpos(0,0)
        game_over.write("You win!", align="center", font=("Helvetica", 48, "normal"))
        
screen.exitonclick()