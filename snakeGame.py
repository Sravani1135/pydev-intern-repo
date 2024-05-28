import turtle
import random
import time

# creating a screen
game_screen = turtle.Screen()
game_screen.title("SNAKE GAME")
game_screen.setup(width=700, height=700)
game_screen.tracer(0)
game_screen.bgcolor("#1d1d1d")

# border creation
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color('red')
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# initial score
score = 0
delay = 0.1

# creating snake
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0, 0)
player.direction = 'stop'

# creating random food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")  # Changed color to red
food.penup()
food.goto(30, 30)

old_food = []

# calculating score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 300)
score_display.write("Score: ", align="center", font=("Arial", 24, "bold"))

# movements
def move_up():
    if player.direction != "down":
        player.direction = "up"

def move_down():
    if player.direction != "up":
        player.direction = "down"

def move_left():
    if player.direction != "right":
        player.direction = "left"

def move_right():
    if player.direction != "left":
        player.direction = "right"

def move_player():
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + 20)

    if player.direction == "down":
        y = player.ycor()
        player.sety(y - 20)

    if player.direction == "left":
        x = player.xcor()
        player.setx(x - 20)

    if player.direction == "right":
        x = player.xcor()
        player.setx(x + 20)

# keyboard
game_screen.listen()
game_screen.onkeypress(move_up, "Up")
game_screen.onkeypress(move_down, "Down")
game_screen.onkeypress(move_left, "Left")
game_screen.onkeypress(move_right, "Right")

# main loop
while True:
    game_screen.update()
    # player and food collision
    if player.distance(food) < 20:
        x = random.randint(-298, 278)
        y = random.randint(-248, 248)
        food.goto(x, y)
        score_display.clear()
        score += 1
        score_display.write("Score: {}".format(score), align="center", font=("Arial", 24, "bold"))
        delay = 0.1
        # creating new foods
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("red")
        new_food.penup()
        old_food.append(new_food)
    # adding ball to player
    for index in range(len(old_food) - 1, 0, -1):
        a = old_food[index - 1].xcor()
        b = old_food[index - 1].ycor()
        old_food[index].goto(a, b)
    if len(old_food) > 0:
        a = player.xcor()
        b = player.ycor()
        old_food[0].goto(a, b)
    move_player()
    # player and border collision
    if (player.xcor() > 300 or player.xcor() < -300 or
            player.ycor() > 250 or player.ycor() < -250):
        time.sleep(1)
        game_screen.clear()
        game_screen.bgcolor("black")  # Change background color to black
        score_display.goto(0, 0)
        score_display.write("Game Over\nYour Score is {}".format(score), align="center", font=("Arial", 30, "bold"))
    # player collision
    for food_piece in old_food:
        if food_piece.distance(player) < 20:
            time.sleep(1)
            game_screen.clear()
            game_screen.bgcolor("black")  # Change background color to black
            score_display.goto(0, 0)
            score_display.write("Game Over\nYour Score is {}".format(score), align="center", font=("Arial", 30, "bold"))
    time.sleep(delay)
