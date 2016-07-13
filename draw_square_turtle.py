import turtle

def draw_shapes():
    window =turtle.Screen()
    window.bgcolor("red")
#square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("green")
    brad.speed(5)
    for i in range(0,4):
       brad.forward(100)
       brad.right(90)
 #circle   
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
#triangle
    sams =turtle.Turtle()
    sams.shape("classic")
    sams.color("black")
    for i in range(0,3):
        sams.forward(100)
        sams.left(240)
    window.exitonclick()
draw_shapes()
