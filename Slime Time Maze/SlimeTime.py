# ------ Import items
import turtle as trtl
import keyboard
import time

# --- Lists
swall = []
outwall = []

wB5 = []
bB5TC5 = []

wC5 = []
bC5TC6 = []
bC5TB5 = []
wC6 = []
bC6TC5 = []



# ----- Screen Set Up
screen = trtl.Screen()
screen.setup(width=683, height=665)

# ------ Import Images
# - Back Ground Tiles
Bg = "D:/CSP/Slime Time Maze/Images/Tiles.gif"
screen.addshape(Bg)
# - Right
idler_image = "D:/CSP/Slime Time Maze/Images/right_idle.gif"
runr_image = "D:/CSP/Slime Time Maze/Images/right_run.gif"
screen.addshape(idler_image)
screen.addshape(runr_image)
# - Left
idlel_image = "D:/CSP/Slime Time Maze/Images/left_idle.gif"
runl_image = "D:/CSP/Slime Time Maze/Images/left_run.gif"
screen.addshape(idlel_image)
screen.addshape(runl_image)
# - Down
idled_image = "D:/CSP/Slime Time Maze/Images/down_idle.gif"
rund_image = "D:/CSP/Slime Time Maze/Images/down_run.gif"
screen.addshape(idled_image)
screen.addshape(rund_image)
# - Up
idleu_image = "D:/CSP/Slime Time Maze/Images/up_idle.gif"
runu_image = "D:/CSP/Slime Time Maze/Images/up_run.gif"
screen.addshape(idleu_image)
screen.addshape(runu_image)

# --- Row / Col Set Up
columnVal = []
rowVal = []

Colum = 369
while (Colum > -447):
  columnVal.append(Colum)
  Colum = Colum - 68
Col0 = columnVal.pop()
Col1 = columnVal.pop()
Col2 = columnVal.pop()
Col3 = columnVal.pop()
Col4 = columnVal.pop()
Col5 = columnVal.pop()
Col6 = columnVal.pop()
Col7 = columnVal.pop()
Col8 = columnVal.pop()
Col9 = columnVal.pop()
Col10 = columnVal.pop()
Col11 = columnVal.pop()

Row = -357.5
while (Row < 422):
  rowVal.append(Row)
  Row = Row + 65
Row0 = rowVal.pop()
Row1 = rowVal.pop()
Row2 = rowVal.pop()
Row3 = rowVal.pop()
Row4 = rowVal.pop()
Row5 = rowVal.pop()
Row6 = rowVal.pop()
Row7 = rowVal.pop()
Row8 = rowVal.pop()
Row9 = rowVal.pop()
Row10 = rowVal.pop()
Row11 = rowVal.pop()
# --- Area Creation Functions
def outwalls():

    for i in range(0, 40):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("black")
        swall.append(wall)
    # ---- Left
    # 1
    wC0R1 = swall.pop()
    wC0R1.goto(Col0, Row1)
    outwall.append(wC0R1)
    # 2
    wC0R2 = swall.pop()
    wC0R2.goto(Col0, Row2)
    outwall.append(wC0R2)
    # 3
    wC0R3 = swall.pop()
    wC0R3.goto(Col0, Row3)
    outwall.append(wC0R3)
    # 4
    wC0R4 = swall.pop()
    wC0R4.goto(Col0, Row4)
    outwall.append(wC0R4)
    # 5
    wC0R5 = swall.pop()
    wC0R5.goto(Col0, Row5)
    outwall.append(wC0R5)
    # 6
    wC0R6 = swall.pop()
    wC0R6.goto(Col0, Row6)
    outwall.append(wC0R6)
    # 7
    wC0R7 = swall.pop()
    wC0R7.goto(Col0, Row7)
    outwall.append(wC0R7)
    # 8
    wC0R8 = swall.pop()
    wC0R8.goto(Col0, Row8)
    outwall.append(wC0R8)
    # 9
    wC0R9 = swall.pop()
    wC0R9.goto(Col0, Row9)
    outwall.append(wC0R9)
    # 10
    wC0R10 = swall.pop()
    wC0R10.goto(Col0, Row10)
    outwall.append(wC0R10)

    # ------ Right

    # 11
    wC11R1 = swall.pop()
    wC11R1.goto(Col11, Row1)
    outwall.append(wC11R1)
    # 12
    wC11R2 = swall.pop()
    wC11R2.goto(Col11, Row2)
    outwall.append(wC11R2)
    # - 13
    wC11R3 = swall.pop()
    wC11R3.goto(Col11, Row3)
    outwall.append(wC11R3)
    # 14
    wC11R4 = swall.pop()
    wC11R4.goto(Col11, Row4)
    outwall.append(wC11R4)
    # - 15
    wC11R5 = swall.pop()
    wC11R5.goto(Col11, Row5)
    outwall.append(wC11R5)
    # - 16
    wC11R6 = swall.pop()
    wC11R6.goto(Col11, Row6)
    outwall.append(wC11R6)
    # 17
    wC11R7 = swall.pop()
    wC11R7.goto(Col11, Row7)
    outwall.append(wC11R7)
    # - 18
    wC11R8 = swall.pop()
    wC11R8.goto(Col11, Row8)
    outwall.append(wC11R8)
    # 19
    wC11R9 = swall.pop()
    wC11R9.goto(Col11, Row9)
    outwall.append(wC11R9)
    # 20
    wC11R10 = swall.pop()
    wC11R10.goto(Col11, Row10)
    outwall.append(wC11R10)

    # ---- Top

    # 21
    wC1R0 = swall.pop()
    wC1R0.goto(Col1, Row0)
    outwall.append(wC1R0)
    # 22
    wC2R0 = swall.pop()
    wC2R0.goto(Col2, Row0)
    outwall.append(wC2R0)
    # 23
    wC3R0 = swall.pop()
    wC3R0.goto(Col3, Row0)
    outwall.append(wC3R0)
    # 24
    wC4R0 = swall.pop()
    wC4R0.goto(Col4, Row0)
    outwall.append(wC4R0)
    # 25
    wC5R0 = swall.pop()
    wC5R0.goto(Col5, Row0)
    outwall.append(wC5R0)
    # 26
    wC6R0 = swall.pop()
    wC6R0.goto(Col6, Row0)
    outwall.append(wC6R0)
    # 27
    wC7R0 = swall.pop()
    wC7R0.goto(Col7, Row0)
    outwall.append(wC7R0)
    # 28
    wC8R0 = swall.pop()
    wC8R0.goto(Col8, Row0)
    outwall.append(wC8R0)
    # 29
    wC9R0 = swall.pop()
    wC9R0.goto(Col9, Row0)
    outwall.append(wC9R0)
    # 30
    wC10R0 = swall.pop()
    wC10R0.goto(Col10, Row0)
    outwall.append(wC10R0)

    # ---- Bottom

    # 31
    wC1R11 = swall.pop()
    wC1R11.goto(Col1, Row11)
    outwall.append(wC1R11)
    # 32
    wC2R11 = swall.pop()
    wC2R11.goto(Col2, Row11)
    outwall.append(wC2R11)
    # 33
    wC3R11 = swall.pop()
    wC3R11.goto(Col3, Row11)
    outwall.append(wC3R11)
    # 34
    wC4R11 = swall.pop()
    wC4R11.goto(Col4, Row11)
    outwall.append(wC4R11)
    # 35
    wC5R11 = swall.pop()
    wC5R11.goto(Col5, Row11)
    outwall.append(wC5R11)
    # 36
    wC6R11 = swall.pop()
    wC6R11.goto(Col6, Row11)
    outwall.append(wC6R11)
    # 37
    wC7R11 = swall.pop()
    wC7R11.goto(Col7, Row11)
    outwall.append(wC7R11)
    # 38
    wC8R11 = swall.pop()
    wC8R11.goto(Col8, Row11)
    outwall.append(wC8R11)
    # 39
    wC9R11 = swall.pop()
    wC9R11.goto(Col9, Row11)
    outwall.append(wC9R11)
    # 40
    wC10R11 = swall.pop()
    wC10R11.goto(Col10, Row11)
    outwall.append(wC10R11)


def aB5():
    for i in range(0, 42):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("black")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col1, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row1)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row2)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row3)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row4)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row4)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row5)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row6)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row6)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row6)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row6)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row7)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row7)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row7)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row7)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row7)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row8)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row8)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row8)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row8)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row9)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row9)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row9)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row9)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row10)
    wB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row10)
    wB5.append(cwall)

    for i in range(0, 5):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("blue")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col1, Row11)
    bB5TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row11)
    bB5TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row11)
    bB5TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row11)
    bB5TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row11)
    bB5TC5.append(cwall)

def aC5():

    for i in range(0, 36):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("black")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col2, Row1)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row1)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row1)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row1)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row1)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row2)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row2)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row2)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row2)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row3)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row3)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row4)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row7)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row8)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row8)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row9)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row9)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row9)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row10)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row10)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row10)
    wC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row10)
    wC5.append(cwall)

    owall = trtl.Turtle()
    owall.shape("square")
    owall.penup()
    owall.turtlesize(3.35)
    owall.color("orange")
    wC5.append(owall)
    owall.goto(Col3, Row3)

    rwall = trtl.Turtle()
    rwall.shape("square")
    rwall.penup()
    rwall.turtlesize(3.35)
    rwall.color("red")
    wC5.append(rwall)
    rwall.goto(Col8, Row3)

    gwall = trtl.Turtle()
    gwall.shape("square")
    gwall.penup()
    gwall.turtlesize(3.35)
    gwall.color("green")
    wC5.append(gwall)
    gwall.goto(Col3, Row8)

    bwall = trtl.Turtle()
    bwall.shape("square")
    bwall.penup()
    bwall.turtlesize(3.35)
    bwall.color("blue")
    wC5.append(bwall)
    bwall.goto(Col8, Row8)

    for i in range(0, 9):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("blue")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col11, Row3)
    bC5TC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col11, Row5)
    bC5TC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col11, Row6)
    bC5TC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col11, Row8)
    bC5TC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row0)
    bC5TB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row0)
    bC5TB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row0)
    bC5TB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row0)
    bC5TB5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row0)
    bC5TB5.append(cwall)
def aC6():

    for i in range(0, 46):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("black")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col2, Row1)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row1)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row1)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row1)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row1)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row2)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row2)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row2)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row2)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row3)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row3)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row4)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row5)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row5)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row5)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row5)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row6)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row6)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row7)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row8)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10, Row9)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col1, Row10)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2, Row10)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6, Row10)
    wC6.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row10)
    wC6.append(cwall)

    for i in range(0, 4):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.35)
        wall.color("blue")
        swall.append(wall)

    cwall = swall.pop()
    cwall.goto(Col0, Row3)
    bC6TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col0, Row5)
    bC6TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col0, Row6)
    bC6TC5.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col0, Row8)
    bC6TC5.append(cwall)


# --- Begin Turtles
BackG = trtl.Turtle(shape = Bg)
slime = trtl.Turtle(shape = idler_image)
slime.penup()
slime.setheading(0)
slime.speed(0)

# --- Movement Creation
run_speedx = 34
run_speedy = 32.5
slSpeed = 0
ImgTime = .05

def left():
  slime.speed(0)
  slime.setheading(180)
  slime.speed(2)
  slime.forward(34)
  slime.shape(runl_image)
  time.sleep(.05)
  slime.shape(idlel_image)

def right():
  slime.speed(0)
  slime.setheading(0)
  slime.speed(2)
  slime.forward(34)
  slime.shape(runr_image)
  time.sleep(.05)
  slime.shape(idler_image)

def up():
  slime.speed(0)
  slime.setheading(90)
  slime.speed(2)
  slime.forward(32.5)
  slime.shape(runu_image)
  time.sleep(.05)
  slime.shape(idleu_image)

def down():
  slime.speed(0)
  slime.setheading(270)
  slime.speed(2)
  slime.forward(32.5)
  slime.shape(rund_image)
  time.sleep(.05)
  slime.shape(idled_image)

# --- Game Variable Set Up
sA1 = False
sA2 = False
sA3 = False
sA4 = False
sA5 = False
sA6 = False
sA7 = False
sA8 = False
sA9 = False

sB1 = False
sB2 = False
sB3 = False
sB4 = False
sB5 = False
sB6 = False
sB7 = False
sB8 = False
sB9 = False

sC1 = False
sC2 = False
sC3 = False
sC4 = False
sC5 = False
sC6 = False
sC7 = False
sC8 = False
sC9 = False

sD1 = False
sD2 = False
sD3 = False
sD4 = False
sD5 = False
sD6 = False
sD7 = False
sD8 = False
sD9 = False

sE1 = False
sE2 = False
sE3 = False
sE4 = False
sE5 = False
sE6 = False
sE7 = False
sE8 = False
sE9 = False

wsA1 = False
wsA2 = False
wsA3 = False
wsA4 = False
wsA5 = False
wsA6 = False
wsA7 = False
wsA8 = False
wsA9 = False

wsB1 = False
wsB2 = False
wsB3 = False
wsB4 = False
wsB5 = False
wsB6 = False
wsB7 = False
wsB8 = False
wsB9 = False

wsC1 = False
wsC2 = False
wsC3 = False
wsC4 = False
wsC5 = False
wsC6 = False
wsC7 = False
wsC8 = False
wsC9 = False

wsD1 = False
wsD2 = False
wsD3 = False
wsD4 = False
wsD5 = False
wsD6 = False
wsD7 = False
wsD8 = False
wsD9 = False

wsE1 = False
wsE2 = False
wsE3 = False
wsE4 = False
wsE5 = False
wsE6 = False
wsE7 = False
wsE8 = False
wsE9 = False

# --- Game Start
screen.tracer(False)

outwalls()
aB5()
for t in wB5:
    t.hideturtle()
for t in bB5TC5:
    t.hideturtle()
aC5()
for t in wC5:
    t.hideturtle()
for t in bC5TC6:
    t.hideturtle()
for t in bC5TB5:
    t.hideturtle()
aC6()
for t in wC6:
    t.hideturtle()
for t in bC6TC5:
    t.hideturtle()
screen.tracer(True)

sC5 = True

while keyboard.is_pressed('p') == False:
    while (1 == 1):
        if keyboard.is_pressed('w') == True:
            up()
            time.sleep(.08)

        if keyboard.is_pressed('a') == True:
            left()
            time.sleep(.08)

        if keyboard.is_pressed('s') == True:
            down()
            time.sleep(.08)

        if keyboard.is_pressed('d') == True:
            right()
            time.sleep(.08)
# - Outer Walls     
        for t in outwall:
            if (0 < (abs(t.ycor() - slime.ycor())) < 45) and (0 < (abs(t.xcor() - slime.xcor())) < 45):
                    Cd = slime.heading()
                    slime.setheading(Cd-180)
                    if (Cd == 90 or Cd == 270):
                        slime.forward(run_speedy)
                    elif (Cd == 180 or Cd == 0):
                        slime.forward(run_speedx)
# - B5
        if sB5:
            print(int(len(outwall)), "C5 -> B5")
            screen.tracer(False)
            for t in wB5:
                t.showturtle()
            for t in bB5TC5:
                t.hideturtle()
            wC1R11 = outwall.pop(30)
            wC3R11 = outwall.pop(31)
            wC5R11 = outwall.pop(32)
            wC6R11 = outwall.pop(32)
            wC8R11 = outwall.pop(33)
            screen.tracer(True)
            sB5 = False
            wsB5 = True
        if wsB5:
            for t in wB5:
                if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
                    Cd = slime.heading()
                    slime.setheading(Cd-180)
                    if (Cd == 90 or Cd == 270):
                        slime.forward(run_speedy)
                    elif (Cd == 180 or Cd == 0):
                        slime.forward(run_speedx)
            for t in bB5TC5:
                if (0 < (abs(t.ycor() - slime.ycor())) < 60) and (0 < (abs(t.xcor() - slime.xcor())) < 60):
                    screen.tracer(False)
                    sC5 = True
                    slime.goto(slime.xcor(), Row1)
                    for t in wB5:
                        t.hideturtle()
                    for t in bB5TC5:
                        t.hideturtle()
                    wsB5 = False
                    outwall.insert(33, wC8R11)
                    outwall.insert(32, wC6R11)
                    outwall.insert(32, wC5R11)
                    outwall.insert(31, wC3R11)
                    outwall.insert(30, wC1R11)
                    screen.tracer(True)

# - C5
        if sC5:
            print(int(len(outwall)), "C6 -> C5")
            screen.tracer(False)
            for t in wC5:
                t.showturtle()
            for t in bC5TC6:
                t.showturtle()
            for t in bC5TB5:
                t.showturtle()
            wC0R1 = outwall.pop(0)
            wC0R2 = outwall.pop(0)
            wC0R5 = outwall.pop(2)
            wC0R6 = outwall.pop(2)
            wC0R8 = outwall.pop(3)
            wC11R3 = outwall.pop(7)
            wC11R5 = outwall.pop(8)
            wC11R6 = outwall.pop(8)
            wC11R8 = outwall.pop(9)
            wC1R0 = outwall.pop(11)
            wC3R0 = outwall.pop(12)
            wC5R0 = outwall.pop(13)
            wC6R0 = outwall.pop(13)
            wC8R0 = outwall.pop(14)
            wC1R11 = outwall.pop(16)
            wC2R11 = outwall.pop(16)
            wC3R11 = outwall.pop(16)
            wC5R11 = outwall.pop(17)
            wC6R11 = outwall.pop(17)
            wC8R11 = outwall.pop(18)
            screen.tracer(True)
            wsC5 = True
            sC5 = False
        if wsC5:
            for t in wC5:
                if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
                    Cd = slime.heading()
                    slime.setheading(Cd-180)
                    if (Cd == 90 or Cd == 270):
                        slime.forward(run_speedy)
                    elif (Cd == 180 or Cd == 0):
                        slime.forward(run_speedx)
        #  - bC5TC6
            for t in bC5TC6:
                if (0 < (abs(t.ycor() - slime.ycor())) < 60) and (0 < (abs(t.xcor() - slime.xcor())) < 60):
                    screen.tracer(False)
                    sC6 = True
                    slime.goto(Col1, slime.ycor())
                    for t in wC5:
                        t.hideturtle()
                    for t in bC5TC6:
                        t.hideturtle()
                    for t in bC5TB5:
                        t.hideturtle()
                    wsC5 = False
                    outwall.insert(18, wC8R11)
                    outwall.insert(17, wC6R11)
                    outwall.insert(17, wC5R11)
                    outwall.insert(16, wC3R11)
                    outwall.insert(16, wC2R11)
                    outwall.insert(16, wC1R11)
                    outwall.insert(14, wC8R0)
                    outwall.insert(13, wC6R0)
                    outwall.insert(13, wC5R0)
                    outwall.insert(12, wC3R0)
                    outwall.insert(11, wC1R0)
                    outwall.insert(9, wC11R8)
                    outwall.insert(8, wC11R6)
                    outwall.insert(8, wC11R5)
                    outwall.insert(7, wC11R3)
                    outwall.insert(3, wC0R8)
                    outwall.insert(2, wC0R6)
                    outwall.insert(2, wC0R5)
                    outwall.insert(0, wC0R2)
                    outwall.insert(0, wC0R1)

        # - bC5TB5
            for t in bC5TB5:
                if (0 < (abs(t.ycor() - slime.ycor())) < 60) and (0 < (abs(t.xcor() - slime.xcor())) < 60):
                    screen.tracer(False)
                    sB5 = True
                    slime.goto(slime.xcor(), Row10)
                    for t in wC5:
                        t.hideturtle()
                    for t in bC5TC6:
                        t.hideturtle()
                    for t in bC5TB5:
                        t.hideturtle()
                    outwall.insert(18, wC8R11)
                    outwall.insert(17, wC6R11)
                    outwall.insert(17, wC5R11)
                    outwall.insert(16, wC3R11)
                    outwall.insert(16, wC2R11)
                    outwall.insert(16, wC1R11)
                    outwall.insert(14, wC8R0)
                    outwall.insert(13, wC6R0)
                    outwall.insert(13, wC5R0)
                    outwall.insert(12, wC3R0)
                    outwall.insert(11, wC1R0)
                    outwall.insert(9, wC11R8)
                    outwall.insert(8, wC11R6)
                    outwall.insert(8, wC11R5)
                    outwall.insert(7, wC11R3)
                    outwall.insert(3, wC0R8)
                    outwall.insert(2, wC0R6)
                    outwall.insert(2, wC0R5)
                    outwall.insert(0, wC0R2)
                    outwall.insert(0, wC0R1)
                    wsC5 = False
                    screen.tracer(True)
# - C6
        if sC6:
            print(int(len(outwall)), "C5 -> C6")
            screen.tracer(False)
            for t in wC6:
                t.showturtle()
            for t in bC6TC5:
                t.showturtle()
            wC11R3 = outwall.pop(2)
            wC11R5 = outwall.pop(3)
            wC11R6 = outwall.pop(3)
            wc11R8 = outwall.pop(4)
            wsC6 = True
            sC6 = False
            screen.tracer(True)
        if wsC6:
            for t in wC6:
                if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
                    Cd = slime.heading()
                    slime.setheading(Cd-180)
                    if (Cd == 90 or Cd == 270):
                        slime.forward(run_speedy)
                    elif (Cd == 180 or Cd == 0):
                        slime.forward(run_speedx)
            for t in bC6TC5:
                if (0 < (abs(t.ycor() - slime.ycor())) < 60) and (0 < (abs(t.xcor() - slime.xcor())) < 60):
                    screen.tracer(False)
                    slime.goto(Col10, slime.ycor())
                    sC5 = True
                    for t in wC6:
                        t.hideturtle()
                    for t in bC6TC5:
                        t.hideturtle()
                    wsC6 = False
                    outwall.insert(4, wc11R8)
                    outwall.insert(3, wC11R6)
                    outwall.insert(3, wC11R5)
                    outwall.insert(2, wC11R3)
                    screen.tracer(True)
screen.mainloop()