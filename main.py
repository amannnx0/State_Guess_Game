import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_state)}/50 correct", prompt="What the state's name?")
    print(ans_state)


    if ans_state in all_state:
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == ans_state]
        t.goto(state.x.item(),state.y.item())
        t.write(ans_state)

screen.exitonclick()