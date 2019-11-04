#This function declare and initialize all global variables
#This function should only be called once
def init():
    global ScreenWidth
    ScreenWidth = 800
    global ScreenHeight
    ScreenHeight = 600
    global ScreenSize
    ScreenSize = (ScreenWidth,ScreenHeight)
    global Screen #Global refernece to display screen
    Screen = 0