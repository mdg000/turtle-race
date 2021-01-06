# 100 Days of Code
# Turtle Racing

from turtle import Turtle, Screen
import random

# screen and race setup
is_race_on = False
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

# create multiple instances of turtle objects, give them different colors and starting positions
y = -100
for i in range(len(colors)):
    my_turt = Turtle(shape="turtle")
    my_turt.penup()
    my_turt.goto(x=-235, y=y)
    my_turt.color(colors[i])
    all_turtles.append(my_turt)
    y += 40

if user_bet:
    is_race_on = True

# race logic
while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 40)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"The winner is {winner}, you guessed right!")
            else:
                print(f"The winner is {winner}, you guessed wrong!")

screen.exitonclick()