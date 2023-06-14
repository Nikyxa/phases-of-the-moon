import turtle

turtle.setup(800, 800)
window = turtle.Screen()
window.bgcolor("blue")


def create_object(form, color, size):
    obj = turtle.Turtle()
    obj.shape(form)
    obj.color(color)
    obj.shapesize(size)
    return obj


shape = create_object("circle", "blue", 20)

shape.penup()
shape.setposition(400, 0)
shape.speed(100)

moon = create_object("circle", "orange", 20)

while True:
    shape.speed(1)
    shape.backward(800)
    shape.hideturtle()
    shape.speed(10)
    shape.setposition(400, 0)
    shape.showturtle()
