from PIL import ImageGrab, ImageOps
import pyautogui as pag
import time
import numpy as np

dinazor = (235,500)
    
def restart():
    pag.click(474,453)
    
def Clicker():
    
    pag.keyDown('space')
    print("Zıplaa")
    time.sleep(0.1)
    pag.keyUp('space')
    


    
def Detector():
    box = (dinazor[0]+120, dinazor[1],
           dinazor[0]+147,  dinazor[1]+20)
    img = ImageGrab.grab(box)
    gray = ImageOps.grayscale(img)
    a = np.array(gray.getcolors())
    print(a.sum())
    return a.sum()


    
def Play():    
    restart()
    while True:
        if(Detector() == 870 ):
            time.sleep(0.1)
            Clicker()
            

Play()