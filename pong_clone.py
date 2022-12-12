# Bong - A Simple Pong Clone in Python 

import turtle

wind = turtle.Screen()
wind.title("Bong - A simple Pong clone, made with Python")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Left side spliff 

splf_l = turtle.Turtle()
splf_l.speed(0)
splf_l.shape("square")
splf_l.color("red")
splf_l.shapesize(stretch_wid=5, stretch_len=1)
splf_l.penup()
splf_l.goto(-350, 0)

# Right side spliff 

splf_r = turtle.Turtle()
splf_r.speed(0)
splf_r.shape("square")
splf_r.color("red")
splf_r.shapesize(stretch_wid=5, stretch_len=1)
splf_r.penup()
splf_r.goto(350, 0)

# create the Bong

bong = turtle.Turtle()
bong.speed(0)
bong.shape("square")
bong.color("red")
bong.penup()
bong.goto(0, 0)
bong.dx = 0.09
bong.dy = 0.09

# Spliffs Movement

def splf_l_up():
	y = splf_l.ycor()
	y += 10
	splf_l.sety(y)

def splf_l_dwn():
	y = splf_l.ycor()
	y -= 10
	splf_l.sety(y)

def splf_r_up():
	y = splf_r.ycor()
	y += 10
	splf_r.sety(y)

def splf_r_dwn():
	y = splf_r.ycor()
	y -= 10
	splf_r.sety(y)

wind.listen()
wind.onkeypress(splf_l_up, "w")
wind.onkeypress(splf_l_dwn, "s")
wind.onkeypress(splf_r_up, "Up")
wind.onkeypress(splf_r_dwn, "Down")



# Game loop 

while True:
	wind.update()

	bong.setx(bong.xcor() + bong.dx)
	bong.sety(bong.ycor() + bong.dy)

	if bong.ycor() > 290:
		bong.sety(290)
		bong.dy *= -1

	if bong.ycor() < -290:
		bong.sety(-290)
		bong.dy *= -1

	if bong.xcor() > 390:
		bong.goto(0, 0)
		bong.dx *= -1

	if bong.xcor() < -390:
		bong.goto(0, 0)
		bong.dx *= -1

