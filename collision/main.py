import turtle
import hitbox
import time
import math

turtle.tracer(0, 0)
window = turtle.Screen()
window.setup(800, 450)
window.listen()

square1 = hitbox.Hitbox(160, 200)
t1 = turtle.Turtle()
t1.shape("square")
t1.shapesize(square1.height / 20, square1.width / 20)
t1.up()
square1.goto(-200, 0)
t1.goto(-200, 0)

square2 = hitbox.Hitbox(80, 40)
t2 = turtle.Turtle()
t2.shape("square")
t2.shapesize(square2.height / 20, square2.width / 20)
t2.up()
square2.goto(200, 0)
t2.goto(200, 0)

p1 = turtle.Turtle()
p1.shape("circle")
p1.color("blue")
p1.shapesize(1/4)
p1.up()

p2 = turtle.Turtle()
p2.shape("circle")
p2.color("blue")
p2.shapesize(1/4)
p2.up()

p3 = turtle.Turtle()
p3.shape("circle")
p3.color("blue")
p3.shapesize(1/4)
p3.up()

p4 = turtle.Turtle()
p4.shape("circle")
p4.color("blue")
p4.shapesize(1/4)
p4.up()

hidden = turtle.Turtle()
hidden.up()
hidden.color("red")
hidden.shape("circle")
hidden.hideturtle()

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
	
def readinfo():
	print()
	print(f"rotation: {square1.rotation}\n"
	      f"position: {square1.xcor}, {square1.ycor}\n"
	      f"p1: {square1.p1()}\n"
	      f"p2: {square1.p2()}\n"
	      f"p3: {square1.p3()}\n"
	      f"p4: {square1.p4()}\n")

window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(turn_left, "q")
window.onkeypress(turn_right, "e")
window.onkeypress(readinfo, "space")

window.onkeyrelease(no_up, "w")
window.onkeyrelease(no_down, "s")
window.onkeyrelease(no_left, "a")
window.onkeyrelease(no_right, "d")
window.onkeyrelease(unturn_left, "q")
window.onkeyrelease(unturn_right, "e")


while True:
	window.update()
	for t in window.turtles():
		t.clearstamps()
	time.sleep(0.01)
	# print()
	# print(f"rotation: {square1.rotation}\n"
	#       f"p1: {square1.p1()}\n"
	#       f"p2: {square1.p2()}\n"
	#       f"p3: {square1.p3()}\n"
	#       f"p4: {square1.p4()}\n")
	
	if up:
		square1.goto(square1.xcor, square1.ycor + 1)
		t1.goto(square1.center())
	if down:
		square1.goto(square1.xcor, square1.ycor - 1)
		t1.goto(square1.center())
	if left:
		square1.goto(square1.xcor - 1, square1.ycor)
		t1.goto(square1.center())
	if right:
		square1.goto(square1.xcor + 1, square1.ycor)
		t1.goto(square1.center())
	if tleft:
		square1.rotation = (square1.rotation + 1) % 360
		t1.left(1)
	if tright:
		square1.rotation = (square1.rotation - 1) % 360
		t1.right(1)
	
	p1.goto(square1.p1())
	p2.goto(square1.p2())
	p3.goto(square1.p3())
	p4.goto(square1.p4())
	
	if square1.collide(square2):
		t1.color("red")
	else:
		t1.color("black")
		
	xsect =  square1.edge1().intersect(square2.edge1())
	if xsect is not None:
		hidden.goto(xsect)
		hidden.stamp()
	