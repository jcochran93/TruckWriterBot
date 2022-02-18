import imp
import pyautogui
import time
import csv
import cv2
import numpy as np
import random
from PIL import ImageGrab
import sys
import os
import config

# os.chdir(os.path.dirname(sys.argv[0]))

def getCSV(path2file, rand=False):
    csvFile = path2file
    
    f = open(csvFile, "r")
    lines = f.readlines()
    if (rand):
        random.shuffle(lines)
    
    f.close()
    return lines

def isTruckWriterOpen():

    manualEntryLink = config.LINK_TO_MANUAL_ICON

    try:
        location = pyautogui.locateOnScreen(manualEntryLink, confidence=0.8, grayscale=False)
        
        pyautogui.moveTo(location[0]+ 75,location[1]-location[1]+1, duration=1)

        pyautogui.click()
    except:
        location = [0,0,0,0]

    return location


def manualEntry(location, name):

    # Clicks Manual Entry Button and enters part name

    pyautogui.click(location[0]+ 75, location[1]+50)# Manual entry click
    time.sleep(.4)
    pyautogui.typewrite(name) #Enter part Name

    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter") # 2 enters to get to price entry
    time.sleep(.2) 

def selectOEM():

    #Selects OEM as Operation Type

    pyautogui.hotkey("down")
    time.sleep(.2)
    pyautogui.hotkey("enter")
    time.sleep(.2)            # Select OEM

def enterPrice(price):
    print(price)
    partPrice = float(price)
    partPrice = "{:.2f}".format(partPrice)
    pyautogui.typewrite(partPrice) #Enter part price

def defaultSaveAndExit():

    # Save Entry with no Labor

    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter") # 2 enters to get to price entry
    time.sleep(.2)
    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter") # 2 enters to get to price entry
    time.sleep(.5)


def main(filePath):

    path2file = filePath

    lines = getCSV(path2file)

    location = isTruckWriterOpen()

    if(location[1] != 0):
        for x in lines[1:]:
            line = x
            part = line.split(",")
            part[2] = part[2].strip('\n')

            manualEntry(location, part[0])
            selectOEM()
            enterPrice(part[1])
            defaultSaveAndExit()

if __name__ == "__main__":
    
    # main()

    isTruckWriterOpen()
