import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import functions

import os

class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("TruckWriter Bot")
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomeScreen, LaunchPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomeScreen)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        homeTitle = tk.Label(self, text="Estimate Entry Bot",
                            pady=10,
                            )
        homeTitle.grid(row=1, column=0, sticky="w")

        homeInstructions = tk.Label(self, text="Step 1: Enter path to csv with format \"Name, Price, QTY\".",
                            pady=10,
                            )
        homeInstructions.grid(row=2, column=0, sticky="w")

        buttonLabel = ttk.Label(self, text="Enter Path to CSV:")
        buttonLabel.grid(row=3, column=0,sticky="w")

        csvPath = ttk.Entry(self)
        csvPath.grid(row=3, column=1,sticky="w")

        enterButton = ttk.Button(self, text="Submit", 
                                command= lambda: self.getPath(csvPath), )
        enterButton.grid(row=3, column=2,sticky="w")

    def getPath(self, csvPath):
        global rawPath
        global isValidPath

        pathToFile = csvPath.get() 
        rawPath = r'{}'.format(pathToFile)
        csvPath.delete(0, tk.END)
        isValidPath = os.path.exists(rawPath)
        
        if(isValidPath):
            self.controller.show_frame(LaunchPage)
        else:
            messagebox.showerror("showerror", "Error: Enter Valid Path to CSV")


# second window frame page1
class LaunchPage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Launch Page")
        label.grid(row = 0, column = 0, sticky="w")

        page1Instructions = tk.Label(self, text="Step 2: Open TruckWriter behine this window. Make sure Manual Entry is visible.",
                            pady=10,
                            )
        page1Instructions.grid(row=1, column=0, sticky="w")        
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Begin Import",
                            command = lambda : self.beginImport())
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Return to Home",
                            command = lambda : controller.show_frame(HomeScreen))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    def beginImport(self):
        functions.main(rawPath)

app = tkinterApp()
app.mainloop()
