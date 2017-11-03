import turtle
from andyFunctionfile import*
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(0)
bob.width(10)
turtle.bgcolor(109, 255, 126)
d = 100
s = 3
a = 360/s + 1
d2 = 25
s2 = 3
a2 = 360/s2 +1

for times in range(175):
    c = (0,times,81+times)
    bob.color(c)
    bob.forward(times)
    bob.right(91)
    c = (64+times, times, 81+times)
    bob.circle(50)
    for times in range(5):
        bob.forward(times)
        bob.right(times)
    c = (64+times, times, 81+times)
    bob.color(c)
    bob.forward(times)
    bob.right(91)
    c = (0,times,81+times)
    bob.circle(50)
    for times in range(5):
        bob.forward(times)
        bob.right(times)

bob.width(10)
jump(bob,227,240)
for times in range(75):
    c = (147, 255, 213)
    bob.color(c)
    bob.forward(times)
    bob.right(a2)
    c =(255, 163, 163)
    bob.color(c)
    bob.circle(d2)

jump(bob,245,-214)
for times in range(75):
    c = (147, 255, 213)
    bob.color(c)
    bob.forward(times)
    bob.right(a2)
    c =(255, 163, 163)
    bob.color(c)
    bob.circle(d2)

jump(bob,-229,241)
for times in range(75):
    c = (147, 255, 213)
    bob.color(c)
    bob.forward(times)
    bob.right(a2)
    c =(255, 163, 163)
    bob.color(c)
    bob.circle(d2)

jump(bob,-239,-242)
for times in range(75):
    c = (147, 255, 213)
    bob.color(c)
    bob.forward(times)
    bob.right(a2)
    c =(255, 163, 163)
    bob.color(c)
    bob.circle(d2)
