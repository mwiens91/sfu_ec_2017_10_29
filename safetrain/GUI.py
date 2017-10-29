#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):
        self.canvas = tk.Canvas(bg='white', height=400, width=400)
        self.canvas.grid()
        self.track0 = self.canvas.create_polygon(0, 50, 0, 60, 250, 60, 250, 50, fill='red')
        self.track1 = self.canvas.create_polygon(10, 90, 10, 100, 250, 100, 250, 90, fill='red')
        self.track0 = self.canvas.create_polygon(175, 0, 175, 400, 185, 400, 185, 0, fill='red')
        self.track1 = self.canvas.create_polygon(215, 0, 215, 400, 225, 400, 225, 0, fill='red')
        self.track0 = self.canvas.create_polygon(0, 310, 0, 320, 400, 320, 400, 310, fill='red')
        self.track1 = self.canvas.create_polygon(0, 350, 0, 360, 400, 360, 400, 350, fill='red')
        #self.station = self.canvas.create_polygon(0, 0, 100, 0, 100, 100, 0, 100, fill='white')

        #self.train = Train()
        #self.train.grid()
        self.startButton = tk.Button(self, text='Start', command=self.quit)
        self.startButton.grid()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)#, padx=40, pady=20)
        self.quitButton.grid()
    #def moveit(self):

'''class Train(tk.Frame):
    def __init__(self):
        self.v = tk.BooleanVar()
        self.enabled = tk.Radiobutton(text="Enabled", variable=self.v, value=True)
        self.disabled = tk.Radiobutton(text="Disabled", variable=self.v, value=False)
        self.stationList = ['1101', '1501', '2101', '2501', '3101', '3501']
        self.stationVar = tk.StringVar()
        self.stationDrop = tk.OptionMenu(self, self.stationVar, *self.stationList)
        self.stopTrain = tk.Button(self, text='Stop Train')
        self.slowTrain = tk.Button(self, text='Slow Train')
        self.stationDrop.grid()
        self.enabled.grid()
        self.disabled.grid()
        self.stopTrain.grid()
        self.slowTrain.grid()'''
