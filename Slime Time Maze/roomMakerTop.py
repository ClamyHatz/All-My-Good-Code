import win32api, win32con

from PIL import Image

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

im = Image.open(r"C:/Users/Lily/Desktop/C4pic.jpg")

out = [[0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0]]

yUp = 0
xUp = 0
amount = 11
while(amount != 0):
    for y in range(56, 1240, 113):
        for x in range(59, 1410, 118):
            r,g,b = im.getpixel((x,y))
            if (1<= yUp <= 9 and xUp == 0):
                if (r in range(0, 150)):
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 1)
                else:
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 2)
            elif (1<= yUp <= 9 and xUp == 11):
                if (r in range(0, 150)):
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 1)
                else:
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 2)
            elif(yUp == 10):
                if (r in range(0, 150)):
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 1)
                else:
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 2)
            elif(yUp == 0):
                if (r in range(0, 150)):
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 1)
                else:
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 2)
            else:
                if (r in range(0, 150)):
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 1)
                else:
                    out[yUp].pop(xUp)
                    out[yUp].insert(xUp, 0)
            print("xUp:")
            print(xUp)
            xUp = xUp + 1
        print("xUp set to 0")
        xUp = 0
        print("yUp")
        print(yUp)
        print(out)
        yUp = yUp + 1
        amount = amount - 1
        print(amount)

print(out)