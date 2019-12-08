import shapes
import turtle
x = 100
y = 100
n = 25

for a in range(4):
    for b in range(4):
        shapes.drawSquare(x - (25 * b),y - (25 * a),n)