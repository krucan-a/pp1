import turtle


def drawSquare(x,y,n):
    pen = turtle.Turtle()
    pen.pu()
    pen.setposition(x,y)
    pen.pd()
    for x in range(4):
        pen.forward(n)
        pen.right(90)
x = 100
y = 100
n = 25

for a in range(4):
    for b in range(4):
        drawSquare(x - (25 * b),y - (25 * a),n)