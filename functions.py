import pyautogui 
import time
import random
import config

#default order of file
nameIndex = 0
priceIndex = 1
bodyIndex = 3
paintIndex = 4


def getCSV(path2file, rand=False):
    csvFile = path2file
    
    f = open(csvFile, "r")
    lines = f.readlines()
    if (rand):
        random.shuffle(lines)
    
    f.close()
    return lines

def getIndeces(line):
    line = line.split(",")
    nameIndex = line.index("Name") 
    priceIndex = line.index("Price")
    try:
        bodyIndex = line.index("Body")
    except:
        bodyIndex = 3
        print("Body labor missing or not labeled.")
    try:
        paintIndex = line.index("Paint")
    except:
        paintIndex = 4
        print("Paint labor missing or not labeled.")  


    return nameIndex, priceIndex, bodyIndex, paintIndex

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
    pyautogui.hotkey("enter")
    time.sleep(.2)

def enterBodyLabor(labor):
    bodyLabor = float(labor)
    bodyLabor = "{:.1f}".format(bodyLabor)
    pyautogui.typewrite(bodyLabor) #Enter body hours
    pyautogui.hotkey("enter")
    time.sleep(.2)

def enterPaintLabor(labor):
    paintLabor = float(labor)
    paintLabor = "{:.1f}".format(paintLabor)
    pyautogui.typewrite(paintLabor) #Enter paint hours
    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter")
    time.sleep(.2)

def exitWithBody():
    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter") 
    time.sleep(.5)

def defaultSaveAndExit():

    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter")
    time.sleep(.2)
    pyautogui.hotkey("enter") # 2 enters to get to price entry
    time.sleep(.5)


def main(filePath):

    path2file = filePath

    lines = getCSV(path2file)

    nameIndex, priceIndex, bodyIndex, paintIndex = getIndeces(lines[0])

    location = isTruckWriterOpen()

    if(location[1] != 0):
        for x in lines[1:]:
            line = x
            line = line.strip("\n")
            part = line.split(",")
            
            while( part[-1] == ''):
                part.remove('')

            manualEntry(location, part[nameIndex])
            selectOEM()
            enterPrice(part[priceIndex])
            if (len(part) == 3 ):
                defaultSaveAndExit()
            elif (len(part) == 4 ):
                enterBodyLabor(part[bodyIndex])
                exitWithBody()
            elif (len(part) == 5 ):
                enterBodyLabor(part[bodyIndex])
                enterPaintLabor(part[paintIndex])


if __name__ == "__main__":
    
    # main()

    isTruckWriterOpen()
