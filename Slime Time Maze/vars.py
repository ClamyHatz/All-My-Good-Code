import slime_make as slm
import turtle as trtl
import ColRow as CR

screen = trtl.Screen()

def hAwall():
  screen.tracer(False)
#   for t in Set.awall:
#       t.hideturtle()
  screen.tracer(True)

# --- Warp commands
def wUp():
  screen.tracer(False)
  slm.slime.goto(slm.slime.xcor(), CR.Row10)
#   for t in Set.wall:
#       t.hideturtle()
  screen.tracer(True)

def wRigth():
  screen.tracer(False)
  slm.slime.goto(CR.Col1, slm.slime.ycor())
#   for t in Set.wall:
#       t.hideturtle()
  screen.tracer(True)

def wLeft():
  screen.tracer(False)
  slm.slime.goto(CR.Col10, slm.slime.ycor())
#   for t in Set.wall:
#       t.hideturtle()
  screen.tracer(True)

def wDown():
  screen.tracer(False)
  slm.slime.goto(slm.slime.xcor(), CR.Row1)
#   for t in Set.wall:
#       t.hideturtle()
  screen.tracer(True)

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