import turtle
import hitbox
import time
import math
import line
import polygon

turtle.tracer(0, 0)
window = turtle.Screen()
window.setup(800, 450)
window.listen()

square2 = polygon.Polygon(8, 100)
square2.rotation = 13
square2.goto(0, 0)

square1 = polygon.Polygon(3, 200)
square1.goto(0, 300)
square1.rotation = 0

draw = turtle.Turtle()
draw.hideturtle()
draw.color("orange")

point = turtle.Turtle()
point.up()
point.shape("circle")
point.color("red")
point.shapesize(0.1)
point.hideturtle()

up = False
down = False
left = False
right = False
tleft = False
tright = False

def go_up():
	global up
	up = True
	
def go_down():
	global down
	down = True
	
def go_left():
	global left
	left = True
	
def go_right():
	global right
	right = True
	
def turn_left():
	global tleft
	tleft = True

def turn_right():
	global tright
	tright = True


def no_up():
	global up
	up = False

def no_down():
	global down
	down = False

def no_left():
	global left
	left = False

def no_right():
	global right
	right = False

def unturn_left():
	global tleft
	tleft = False

def unturn_right():
	global tright
	tright = False
	
def pause():
	square1.uncollide(square2)
	
def show(shape, color="black"):
	global draw
	draw.up()
	draw.color(color)
	draw.goto(shape.vertices()[0])
	draw.down()
	
	for i in range(len(shape.vertices())):
		draw.goto(shape.vertices()[(i + 1) % len(shape.vertices())])
		
def showLine(line, color="black"):
	global draw
	
	draw.up()
	draw.color(color)
	draw.goto(line.p1)
	draw.down()
	draw.goto(line.p2)

window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(turn_left, "q")
window.onkeypress(turn_right, "e")
window.onkeypress(pause, "space")

window.onkeyrelease(no_up, "w")
window.onkeyrelease(no_down, "s")
window.onkeyrelease(no_left, "a")
window.onkeyrelease(no_right, "d")
window.onkeyrelease(unturn_left, "q")
window.onkeyrelease(unturn_right, "e")

force = 1
timestamp = time.time()
while True:
	while (time.time() - timestamp) < 0.01:
		time.sleep(0.001)

	timestamp = time.time()
	
	draw.clear()
	show(square1)
	show(square2)
	
	window.update()
	
	for t in window.turtles():
		t.clearstamps()

	if up:
		square1.goto(square1.xcor(), square1.ycor() + force)
	if down:
		square1.goto(square1.xcor(), square1.ycor() - force)
	if left:
		square1.goto(square1.xcor() - force, square1.ycor())
	if right:
		square1.goto(square1.xcor() + force, square1.ycor())
	if tleft:
		square1.rotation = (square1.rotation + 1) % 360
	if tright:
		square1.rotation = (square1.rotation - 1) % 360
	
	impact = square1.collision(square2)
	if impact:
		point.goto(impact)
		point.stamp()