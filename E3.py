import turtle as trtl
import ColRow as CR

screen = trtl.Screen()

# ---- Call Lists
warp1 = []
warp2 = []
warp3 = []
warp4 = []
wall = []
# --------------

swall = []
warp = []
cwall = []

walls = [[2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2], [2, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2], [2, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 
2], [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 2], [2, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 2], [2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
2, 2]]

size = 144

goTime = 0
startTime = 0

nextGo = 0

def make(i):
    if (i == 1):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("black")
        swall.append(wall)
    elif (i == 2):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("blue")
        warp.append(wall)

def place (i,x,y):
    if (x == 0):
        big(x, y, i)
    elif (x == 1):
        big(x, y, i)
    elif (x == 2):
        big(x, y, i)
    elif (x == 3):
        big(x, y, i)
    elif (x == 4):
        big(x, y, i)
    elif (x == 5):
        big(x, y, i)
    elif (x == 6):
        big(x, y, i)
    elif (x == 7):
        big(x, y, i)
    elif (x == 8):
        big(x, y, i)
    elif (x == 9):
        big(x, y, i)
    elif (x == 10):
        big(x, y, i)
    elif (x == 11):
        big(x, y, i)

def big (x,y,i):
    if (y == 0):
        smallBig(i,x,y)
    elif (y == 1):
        smallBig(i,x,y)
    elif (y == 2):
        smallBig(i,x,y)
    elif (y == 3):
        smallBig(i,x,y)
    elif (y == 4):
        smallBig(i,x,y)
    elif (y == 5):
        smallBig(i,x,y)
    elif (y == 6):
        smallBig(i,x,y)
    elif (y == 7):
        smallBig(i,x,y)
    elif (y == 8):
        smallBig(i,x,y)
    elif (y == 9):
        smallBig(i,x,y)
    elif (y == 10):
        smallBig(i,x,y)
    elif (y == 11):
        smallBig(i,x,y)

def smallBig(i,x,y):
    if (i == 1):
        cCol = CR.Col.pop(x)
        cRow = CR.Rowl.pop(y)
        cwall = swall.pop()
        cwall.goto(cCol, cRow)
        wall.append(cwall)
        CR.Col.insert(x, cCol)
        CR.Rowl.insert(y, cRow)

    elif (i == 2 and y == 0):
        cCol = CR.Col.pop(x)
        cRow = CR.Rowl.pop(y)
        cwall = warp.pop()
        cwall.goto(cCol, cRow)
        warp1.append(cwall)
        CR.Col.insert(x, cCol)
        CR.Rowl.insert(y, cRow)

    elif (i == 2 and 1<= y <= 10 and x == 0):
        cCol = CR.Col.pop(x)
        cRow = CR.Rowl.pop(y)
        cwall = warp.pop()
        cwall.goto(cCol, cRow)
        warp2.append(cwall)
        CR.Col.insert(x, cCol)
        CR.Rowl.insert(y, cRow)
    
    elif (i == 2 and 1<= y <= 10 and x == 11):
        cCol = CR.Col.pop(x)
        cRow = CR.Rowl.pop(y)
        cwall = warp.pop()
        cwall.goto(cCol, cRow)
        warp3.append(cwall)
        CR.Col.insert(x, cCol)
        CR.Rowl.insert(y, cRow)

    elif (i == 2 and y == 11):
        cCol = CR.Col.pop(x)
        cRow = CR.Rowl.pop(y)
        cwall = warp.pop()
        cwall.goto(cCol, cRow)
        warp4.append(cwall)
        CR.Col.insert(x, cCol)
        CR.Rowl.insert(y, cRow)

startTime = 0
stopTime = 0

screen.tracer(False)
while (stopTime != size):
    where = walls[nextGo].pop(goTime)
    walls[nextGo].insert(goTime, where)
    make(where)
    goTime = goTime + 1
    stopTime = stopTime + 1
    if (goTime == 12):
        goTime = 0
        nextGo = nextGo + 1

nextGo = 0
someTime = 0

while (someTime != 144): 
    where = walls[nextGo].pop(startTime)
    walls[nextGo].insert(startTime, where)
    place(where, startTime, nextGo)
    startTime = startTime + 1
    someTime = someTime + 1
    if (startTime == 12):
        startTime = 0
        nextGo = nextGo + 1

for t in wall:
  t.hideturtle()

screen.tracer(True)
