# ------ Import items
import turtle as trtl
import keyboard
import time
import ColRow as CR
import image_creation as IC
# --- Set up screen
screen = trtl.Screen()
screen.setup(width=683, height=650)
screen.tracer(False)
# ------ Import Rooms
import A1, A2, A3, A4, A5
import B1, B2, B3, B4, B5
import C1, C2, C3, C4, C5, C6
import D1, D2, D3, D4, D5
import E1, E2, E3, E4, E5
# --- Lists
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
sC5 = True
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

# ----- Var Set Up
Set = ""
num = ""
darkNumb = 0

# --- Begin Turtles
BackG = trtl.Turtle(shape = IC.Bg)
slime = trtl.Turtle(shape = IC.idler_image)
slime.penup()
slime.setheading(0)
slime.speed(0)
dark1s = trtl.Turtle(shape = IC.dark1)
dark1s.penup()
dark1s.setheading(0)
dark1s.speed(0)
dark2s = trtl.Turtle(shape = IC.dark2)
dark2s.penup()
dark2s.setheading(0)
dark2s.speed(0)
dark3s = trtl.Turtle(shape = IC.dark3)
dark3s.penup()
dark3s.setheading(0)
dark3s.speed(0)
dark4s = trtl.Turtle(shape = IC.dark4)
dark4s.penup()
dark4s.setheading(0)
dark4s.speed(0)


# --- Movement Creation
run_speedx = 34
run_speedy = 32.5
slSpeed = 0
ImgTime = .05

# ------- Special Methods
def Coldie():
  for t in Set.wall:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        Cd = slime.heading()
        slime.setheading(Cd-180)
        dark1s.setheading(Cd-180)
        if (Cd == 90 or Cd == 270):
          slime.forward(run_speedy)
          dark1s.goto(slime.xcor(), slime.ycor())
        elif (Cd == 180 or Cd == 0):
          slime.forward(run_speedx)
          dark1s.goto(slime.xcor(), slime.ycor())

def shower():
  screen.tracer(False)
  for t in Set.wall:
      t.showturtle()
  screen.tracer(True)

def hAwall():
  screen.tracer(False)
  for t in Set.awall:
      t.hideturtle()
  screen.tracer(True)

def darkis0():
  dark1s.hideturtle()
  dark2s.hideturtle()
  dark3s.hideturtle()
  dark4s.hideturtle()

def darkis1():
  dark1s.showturtle()
  dark2s.hideturtle()
  dark3s.hideturtle()
  dark4s.hideturtle()

def darkis2():
  dark1s.hideturtle()
  dark2s.showturtle()
  dark3s.hideturtle()
  dark4s.hideturtle()

def darkis3():
  dark1s.hideturtle()
  dark2s.hideturtle()
  dark3s.showturtle()
  dark4s.hideturtle()

def darkis4():
  dark1s.hideturtle()
  dark2s.hideturtle()
  dark3s.hideturtle()
  dark4s.showturtle()

def darkMove():
  dark1s.goto(slime.xcor(), slime.ycor())
  dark2s.goto(slime.xcor(), slime.ycor())
  dark3s.goto(slime.xcor(), slime.ycor())
  dark4s.goto(slime.xcor(), slime.ycor())

# ---- move
def left():
  screen.tracer(False)
  slime.speed(0)
  slime.setheading(180)
  slime.speed(2)
  slime.forward(34)
  darkMove()
  screen.tracer(True)
  slime.shape(IC.runl_image)
  time.sleep(.05)
  slime.shape(IC.idlel_image)

def right():
  screen.tracer(False)
  slime.speed(0)
  slime.setheading(0)
  slime.speed(2)
  slime.forward(34)
  darkMove()
  screen.tracer(True)
  slime.shape(IC.runr_image)
  time.sleep(.05)
  slime.shape(IC.idler_image)

def up():
  screen.tracer(False)
  slime.speed(0)
  slime.setheading(90)
  slime.speed(2)
  slime.forward(32.5)
  darkMove()
  screen.tracer(True)
  slime.shape(IC.runu_image)
  time.sleep(.05)
  slime.shape(IC.idleu_image)

def down():
  screen.tracer(False)
  slime.speed(0)
  slime.setheading(270)
  slime.speed(2)
  slime.forward(32.5)
  darkMove()
  screen.tracer(True)
  slime.shape(IC.rund_image)
  time.sleep(.05)
  slime.shape(IC.idled_image)



# --- Warp commands
def wUp():
  screen.tracer(False)
  slime.goto(slime.xcor(), CR.Row10)
  darkMove()
  for t in Set.wall:
      t.hideturtle()
  screen.tracer(True)

def wRigth():
  screen.tracer(False)
  slime.goto(CR.Col1, slime.ycor())
  darkMove()
  for t in Set.wall:
      t.hideturtle()
  screen.tracer(True)

def wLeft():
  screen.tracer(False)
  slime.goto(CR.Col10, slime.ycor())
  darkMove()
  for t in Set.wall:
      t.hideturtle()
  screen.tracer(True)

def wDown():
  screen.tracer(False)
  slime.goto(slime.xcor(), CR.Row1)
  darkMove()
  for t in Set.wall:
      t.hideturtle()
  screen.tracer(True)

screen.tracer(True)

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
# - A1
  if sA1:
    darkis4()
    Set = A1
    shower()
    Coldie()
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sA2 = True
        sA1 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sB1 = True
        sA1 = False
# - A2
  if sA2:
    darkis3()
    Set = A2
    shower()
    Coldie()
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sA1 = True
        sA2 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sA3 = True
        sA2 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sB2 = True
        sA2 = False
# - A3
  if sA3:
    darkis2()
    Set = A3
    shower()
    Coldie()
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sA2 = True
        sA3 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sA4 = True
        sA3 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sB3 = True
        sA3 = False
# - A4
  if sA4:
    darkis1()
    Set = A4
    shower()
    Coldie()
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sA3 = True
        sA4 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sA5 = True
        sA4 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sB4 = True
        sA4 = False
# - A5
  if sA5:
    darkis0()
    Set = A5
    shower()
    Coldie()
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sA4 = True
        sA5 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sA6 = True
        sA5 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sB5 = True
        sA5 = False
# - B1
  if sB1:
    darkis3()
    Set = B1
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sA1 = True
        sB1 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sB2 = True
        sB1 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sC1 = True
        sB1 = False
# - B2
  if sB2:
    darkis2()
    Set = B2
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sA2 = True
        sB2 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sB1 = True
        sB2 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sB3 = True
        sB2 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sC2 = True
        sB2 = False
# - B3
  if sB3:
    darkis1()
    Set = B3
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sA3 = True
        sB3 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sB2 = True
        sB3 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sB4 = True
        sB3 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sC3 = True
        sB3 = False
# - B4
  if sB4:
    darkis0()
    Set = B4
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sA4 = True
        sB4 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sB3 = True
        sB4 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sB5 = True
        sB4 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sC4 = True
        sB4 = False
# - B5
  if sB5:
    darkis0()
    Set = B5
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sA5 = True
        sB5 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sB4 = True
        sB5 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sB6 = True
        sB5 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sC5 = True
        sB5 = False
# - C1
  if sC1:
    darkis2()
    Set = C1
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sB1 = True
        sC1 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sC2 = True
        sC1 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sD1 = True
        sC1 = False
# - C2
  if sC2:
    darkis1()
    Set = C2
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sB2 = True
        sC2 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sC1 = True
        sC2 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sC3 = True
        sC2 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sD2 = True
        sC2 = False
# - C3
  if sC3:
    darkis0()
    Set = C3
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sB3 = True
        sC3 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sC2 = True
        sC3 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sC4 = True
        sC3 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sD3 = True
        sC3 = False
# - C4
  if sC4:
    darkis0()
    Set = C4
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sB4 = True
        sC4 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sC3 = True
        sC4 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sC5 = True
        sC4 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sD4 = True
        sC4 = False
# - C5 (Room 1)
  if sC5:
    darkis0()
    Set = C5
    shower()
    screen.tracer(False)
    for t in Set.awall:
        t.showturtle()
    screen.tracer(True)
    Coldie()
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        hAwall()
        sD5 = True
        sC5 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        hAwall()
        sC6 = True
        sC5 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        hAwall()
        sC4 = True
        sC5 = False
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        hAwall()
        sB5 = True
        sC5 = False
# - C6
  if sC6:
    darkis0()
    Set = C6
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sB6 = True
        sC6 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sC5 = True
        sC6 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sC7 = True
        sC6 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sD5 = True
        sC6 = False
# - D1
  if sD1:
    darkis3()
    Set = D1
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sC1 = True
        sD1 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sD2 = True
        sD1 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sE1 = True
        sD1 = False
# - D2
  if sD2:
    darkis2()
    Set = D2
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sC2 = True
        sD2 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sD1 = True
        sD2 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sD3 = True
        sD2 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sE2 = True
        sD2 = False
# - D3
  if sD3:
    darkis1()
    Set = D3
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sC3 = True
        sD3 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sD2 = True
        sD3 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sD4 = True
        sD3 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sE3 = True
        sD3 = False
# - D4
  if sD4:
    darkis0()
    Set = D4
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sC4 = True
        sD4 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sD3 = True
        sD4 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sD5 = True
        sD4 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sE4 = True
        sD4 = False
# - D5
  if sD5:
    darkis0()
    Set = D5
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sC5 = True
        sD5 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sD4 = True
        sD5 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sD6 = True
        sD5 = False
    for t in Set.warp4:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wDown()
        sE5 = True
        sD5 = False
# - E1
  if sE1:
    darkis4()
    Set = E1
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sD1 = True
        sE1 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sE2 = True
        sE1 = False
# - E2
  if sE2:
    darkis3()
    Set = E2
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sD2 = True
        sE2 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sE1 = True
        sE2 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sE3 = True
        sE2 = False
# - E3
  if sE3:
    darkis2()
    Set = E3
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sD3 = True
        sE3 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sE2 = True
        sE3 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sE4 = True
        sE3 = False
# - E4
  if sE4:
    darkis1()
    Set = E4
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sD4 = True
        sE4 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sE3 = True
        sE4 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sE5 = True
        sE4 = False
# - E5
  if sE5:
    darkis0()
    Set = E5
    shower()
    Coldie()
    for t in Set.warp1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wUp()
        sD5 = True
        sE5 = False
    for t in Set.warp2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wLeft()
        sE4 = True
        sE5 = False
    for t in Set.warp3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        wRigth()
        sE6 = True
        sE5 = False
