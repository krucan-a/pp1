import turtle

pen = turtle.Turtle()

def drawSquare(x,y,n):
    pen.pu()
    pen.setposition(x,y)
    pen.pd()
    for x in range(4):
        pen.forward(n)
        pen.right(90)

def drawCircle(x,y,r):
    pen.pu()
    pen.setposition(x,y)
    pen.pd()
    pen.circle(r)

def drawEquilateralTriangle(x,y,m):
    pen.pu()
    pen.setposition(x,y)
    pen.pd()
    for x in range(3):
        pen.forward(m)
        pen.left(120)

def drawStar(x,y,m):
    pen.pu()
    pen.setposition(x,y)
    pen.pd()
    pen.right(36)
    for x in range(5):
        pen.forward(m)
        pen.left(144)
        pen.forward(m)
        pen.right(72)
