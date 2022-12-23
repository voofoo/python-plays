import turtle
import random
import time
import os

#delay = 0.1
points = 0
high_score = 0
lives = 10

wn = turtle.Screen()
wn.title("Falling Skies Clone")
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("good_guy.gif")
wn.register_shape("bad_guy.gif")
wn.register_shape("player_right.gif")
wn.register_shape("player_left.gif")

# Add player

player = turtle.Turtle()
player.speed(0)
player.shape("player_right.gif")
player.color("white")
player.penup()
player.goto(0, -240)
player.direction = "stop"

# Create a list of good guys
good_guys = []

# Add the good guys
for _ in range(10):
	good_guy = turtle.Turtle()
	good_guy.speed(0)
	good_guy.shape("good_guy.gif")
	good_guy.color("blue")
	good_guy.penup()
	good_guy.goto(-100, 250)
	good_guy.speed = random.uniform(0.1, 0.33)
	good_guys.append(good_guy)
	#good_guy.direction = "stop"

# Create a list of bad guys
bad_guys = []

# Add the bad guys
for _ in range(10):
	bad_guy = turtle.Turtle()
	bad_guy.speed(0)
	bad_guy.shape("bad_guy.gif")
	bad_guy.color("red")
	bad_guy.penup()
	bad_guy.goto(100, 250)
	bad_guy.speed = random.uniform(0.1, 0.33)
	bad_guys.append(bad_guy)
	#bad_guy.direction = "stop"

#Scorecard

score = turtle.Turtle()
score.speed(0)
score.shape("circle")
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0, 260)
font = ("Courier", 18, "normal")
score.write("Points: {} | Lives: {} | High Score: {}".format(points, lives, high_score), align="center", font=font)

# Functions

def go_left():
	player.direction = "left"
	player.shape("player_left.gif")

def go_right():
	player.direction = "right"
	player.shape("player_right.gif")

# keyboard bindings

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Game Loop

while True:
	# Update screen
	wn.update()

	# Move the player
	if player.direction == "left":
		x = player.xcor()
		x -= 0.3
		player.setx(x)

	if player.direction == "right":
		x = player.xcor()
		x += 0.3
		player.setx(x)

	# Move good guys
	for good_guy in good_guys:
		y = good_guy.ycor()
		y -= good_guy.speed
		good_guy.sety(y)

		# Make good guy come back from top of screen
		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x, y)

		# Check for collision with player
		if player.distance(good_guy) < 20:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x, y)
			points += 1
			os.system("aplay points_plus.wav&")

			if points > high_score:
				high_score = points

			score.clear()
			score.write("Points: {} | Lives: {} | High Score: {}".format(points, lives, high_score), align="center", font=font)

	# Move bad guys
	for bad_guy in bad_guys:
		y = bad_guy.ycor()
		y -= bad_guy.speed
		bad_guy.sety(y)

		# Make bad guy come back from top of screen
		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			bad_guy.goto(x, y)

		# Check for collision with player
		if player.distance(bad_guy) < 20:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			bad_guy.goto(x, y)
			points -= 1
			lives -= 1
			os.system("aplay points_minus.wav&")


			score.clear()
			score.write("Points: {} | Lives: {} | High Score: {}".format(points, lives, high_score), align="center",font=("Courier", 16, "normal"))






wn.mainloop()