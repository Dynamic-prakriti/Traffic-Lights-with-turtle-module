#TrafficLight

import turtle
import time

wn = turtle.Screen()
wn.title("Traffic Lights by Dynamic PT")
wn.bgcolor("black")


#Draw box 
draw = turtle.Turtle()
draw.color("White")
draw.width(9)
draw.hideturtle()
draw.penup()
draw.goto(-60,60)
draw.pendown()
draw.forward(120) #pixels
draw.right(90) #degree
draw.forward(240)
draw.right(90)
draw.forward(120)
draw.right(90)
draw.forward(240)


#red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0,20)

#yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0,-50)

#green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0,-130)


while True:
  red_light.color("red")
  time.sleep(3)

  red_light.color("grey")
  yellow_light.color("yellow")
  time.sleep(2)

  yellow_light.color("grey")
  green_light.color("green")
  time.sleep(4)

  green_light.color("grey")

turtle.done()
