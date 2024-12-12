from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(550,550)
screen.bgcolor("black")



pong1 = Turtle()
pong2 = Turtle()
ball = Turtle()


pong1.shape("square")
pong1.color("white")
pong1.shapesize(5,0.5)
pong1.penup()


pong2.shapesize(5,0.5)
pong2.color("white")
pong2.shape("square")
pong2.penup()

pong1.setposition(-300,0)
pong2.setposition(300,0)


ball.shape("circle")
ball.shapesize(0.5,0.5)
ball.color("white")

def flytta_bollen():
	ball_x = ball.xcor() + 10
	ball_y = ball.ycor() + 10
	ball.goto(ball_x, ball_y)
	
def flytta_upp2():
	ny_plats = pong2.ycor() + 20
	pong2.goto(pong2.xcor(), ny_plats)

def flytta_upp1():
	ny_plats = pong1.ycor() + 20
	pong1.goto(pong1.xcor(), ny_plats)

def flytta_ner1():
	ny_plats = pong1.ycor() - 20
	pong1.goto(pong1.xcor(), ny_plats)

def flytta_ner2():
	ny_plats = pong2.ycor() - 20
	pong2.goto(pong2.xcor(), ny_plats)

ball.penup()



screen.onkey(flytta_upp1, "w")
screen.onkey(flytta_upp2, "Up")
screen.onkey(flytta_ner1, "s")
screen.onkey(flytta_ner2, "Down")
screen.listen()

game_is_on = True

while game_is_on == True:
	flytta_bollen()

	if ball.xcor() < -320 or ball.xcor() > 320:
		ball.hideturtle()
		ball.setposition(0,0)
		ball.showturtle()
	elif ball.ycor() < -320 or ball.ycor() > 320:
		ball.hideturtle()
		ball.setposition(0,0)
		ball.showturtle
	if ball.ycor() < -300 or ball.ycor() > 300:
		ball.speed(- 10)


screen.exitonclick()