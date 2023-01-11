from bottle import route, run, template, static_file
from datetime import datetime
import random
import threading, time, os
import plotly.express as px
import pandas as pd

class GUI:
    def __init__(self):
        # Data properties
        self.data_path = 'D:\\Studium\\7_Semester\\SOM\\SOM-Team1\\Projekt1\\Data.csv'
        self.data_name = 'Data.csv'
    def plot(self, data, ylabel):
        if os.path.exists(self.data_path):
            df_hum = pd.read_csv(self.data_path)
            plot_hum = px.line(x=df_hum['Datetime'], y=df_hum[data], labels=dict(x="", y=ylabel))
            return plot_hum.to_html()
        else:
            return "Keine Daten vorhanden. Bitte vergewissern Sie sich, das SensorDaten.py auf dem Raspberry läuft und das der Datei-Pfad und der Name der CSV Datei in SensorDaten.py und GUI.py identisch sind "

    @route('/')
    def menu():
        return template('menu')

    @route('/downloads')
    def posted():
        return template('downloads')

    @route('/static/<filename>')
    def server_static(filename):
        return static_file(filename, root='./')

    @route('/temperatur')
    def temperatur():
        return template('temperatur'), GUI.plot(GUI(), 'Temperatur', "Temperatur [°C]")

    @route('/luftfeuchtigkeit')
    def humidity():
        return template('luftfeuchtigkeit'), GUI.plot(GUI(), 'Feuchtigkeit', "Luftfeuchtigkeit [%]")

    @route('/livedaten')
    def livedaten():
        now = datetime.now()
        current_time = now.strftime("am %d.%m.%Y um %H:%M:%S")
        print("Current Time =", current_time)
        temp_ran = random.randint(15, 25)
        hum_ran = random.randint(40, 60)
        return template('livedaten', temp=temp_ran, hum=hum_ran, time=current_time)

run(host='localhost', port=8080, reloader=True)