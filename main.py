from turtle import Turtle, Screen
import random
screen = Screen()


def winner_dialogue(betting, win_color):
    if betting == win_color:
        print("Congratulation ,You Win!")
    else:
        print(f"You lose! winner is | {win_color.capitalize()}Turtle |")


colour = ["red", "blue", "green", "black"]
all_Turtle = []
y_coordinate = 115
for color in colour:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setpos(x=-320, y=y_coordinate)
    y_coordinate -= 70
    all_Turtle.append(new_turtle)


user_bet = screen.textinput("Bet Selection", "Which Turtle you want to Bet").lower()
screen.delay(100)


if user_bet:
    is_going = True

while is_going:
    for tur in all_Turtle:
        tur.forward(random.randint(5, 25))
        x_coordinate = tur.xcor()
        if x_coordinate > 320:
            winning_color = tur.pencolor()
            winner_dialogue(user_bet, winning_color)
            is_going = False


screen.exitonclick()
