import turtle

#Global setup
turtle.title("Pattern Maker")
turtle.bgcolor("grey")
turtle.setup(600,600)
turtle.shape("turtle")
#end of Global setup

screen = turtle.Screen()

def draw_square(some_turtle):
  some_turtle.forward(200)
  some_turtle.right(90)

def draw_shapes():
  brad = turtle.Turtle(shape = "turtle")
  brad.color("green")
  brad.goto(150, 150)
  brad.pensize(3)
  brad.speed(6)

  for _ in range(36):
    draw_square(brad)
    brad.right(1)
  
  angie = turtle.Turtle(shape = "turtle")
  angie.color("purple")
  angie.pensize(4)
  angie.speed(4)

  size = 1

  for _ in range(300):
    angie.forward(size)
    angie.right(93)
    size += 1

screen.onkey(draw_shapes, "d")
screen.listen()

turtle.done()
