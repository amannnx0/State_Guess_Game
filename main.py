import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

ans_state = screen.textinput(title="Give it a guess", prompt="What the state's name?")
print(ans_state)


if ans_state in all_state:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[data.state == ans_state]
    t.goto(state.x.item(),state.y.item())
    t.write(ans_state)

screen.exitonclick()