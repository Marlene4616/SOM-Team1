'''====================== '''
#                 import
'''====================== '''

#csv
import pandas as pd

#GUI
import tkinter
from tkinter import *
from tkinter import filedialog

#plot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#Website
import webbrowser



'''====================== '''
#                 Class
'''====================== '''

class gui_python:

    def __init__(self):
#initialize Window
        self.window = tkinter.Tk()
        self.window.wm_title("Seikreativ")
        self.filename = ""
# variables
        self.Temperatur = ""
        self.Feuchtigkeit = ""
        self.DateTime = ""
        self.Website = 'http://141.22.36.123:8080/'

# Run
        self.run()

    def run(self):
        self.browsefiles()
        self.pack_text("avgTemp", self.average(self.Temperatur), tkinter.LEFT)
        self.pack_text("avgHumi", self.average(self.Feuchtigkeit), tkinter.RIGHT)
        self.pack_buttons()
        tkinter.mainloop()

# data handling
    def browsefiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.csv*"),
                                                         ("all files",
                                                          "*.*")))
        self.read_csv()

    def read_csv(self):
        data = pd.read_csv(self.filename)
        self.DateTime = data.Datetime
        self.Temperatur = data.Temperatur
        self.Feuchtigkeit = data.Feuchtigkeit
        self.plot()


# Plot
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.DateTime, self.Temperatur)
        ax.set_ylabel('Temeratur [°C]')
        ax.set_xlabel('Datum und Uhrzeit')
        ax.tick_params(axis='x', rotation=45)
        self.pack_canvas(fig)

    def pack_canvas(self, fig):
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Text
    def pack_text(self, title, averaged, pos):
        if title == "avgTemp":
            text = Label(text=f'The average temperatur is {averaged} °C ')
            text.pack()
        elif title == "avgHumi":
            text = Label(text=f'The average humidity is {averaged} g/m3')
        else:
            text = Label(text='Error')

        text.pack(side=pos)

#Buttons
    def pack_buttons(self):
        cmd_go2web = Button(self.window, text="Web", command=self.OpenWeb)
        cmd_go2web.pack()

#Website
    def OpenWeb(self):
        webbrowser.open(self.Website, new=2)

#Calculations
    def average(self, column):
        return sum(column)/len(column)


'''====================== '''
#                Call Class
'''====================== '''
#x = gui_python()

