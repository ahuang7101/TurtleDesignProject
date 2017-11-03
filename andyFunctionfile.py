#myFunction file
def polygon(t,s,d):
    a = 360/s
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)

    t.end_fill()
def polygon2(t,s,d):
    a = 360/s
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):#variables for the values
#that the function polygon needs
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)

def circli(t,r):
    t.begin_fill()
    t.circle(r)
    t.end_fill()


