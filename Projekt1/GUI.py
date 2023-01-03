# This class start a Web-GUI, to present the data from the class "SensorDaten"
# URL: http://141.22.36.123:8080/
from bottle import route, run, template, static_file
import threading, time, os
import plotly.express as px
import pandas as pd
from SensorDaten import SensorDaten


class GUI:

    def __init__(self):
        # server properties
        self.host = '0.0.0.0'
        self.port = 8080

        # Data properties
        self.data_path = '/home/pi/som-gruppe_5/Projekt1/Data.csv'
        self.data_name = 'Data.csv'

    def plot(self, data, ylabel):
        if os.path.exists(self.data_name) == True:
            df_hum = pd.read_csv(self.data_path)
            plot_hum = px.line(x=df_hum['Datetime'], y=df_hum[data], labels=dict(x="", y=ylabel))
            return plot_hum.to_html()
        else:
            return "Keine Daten vorhanden. Bitte vergewissern Sie sich, das SensorDaten.py auf dem Raspberry läuft und das der Datei-Pfad und der Name der CSV Datei in SensorDaten.py und GUI.py identisch sind "

    def background_server_function(self):
        run(host=self.host, port=self.port, debug=True, reloader=True)

    @route('/')
    def menu():
        return template('menu')

    @route('/downloads')
    def posted():
        return template('downloads')

    # folgendes sagt bottle wo es alle Dateien die im Ordner Projekt1 gespeichert sind finden kann
    @route('/static/<filename>')
    def server_static(filename):
        return static_file(filename, root='./')

    @route('/luftfeuchtigkeit')
    def hum():
        return template('luftfeuchtigkeit'), GUI.plot(GUI(),'Feuchtigkeit', "Luftfeuchtigkeit [%]")

    @route('/temperatur')
    def temp():
        return template('temperatur'), GUI.plot(GUI(),'Temperatur', "Temperatur [°C]")

    @route('/livedaten')
    def livedaten():
        data = SensorDaten()
        return template('livedaten', temp=data.temp, hum=data.hum, time=data.time.replace(microsecond=0))


    def run(self):
        threading.Thread(target=self.background_server_function, daemon=True).start()
        while True:
            print('Server is active in background')
            time.sleep(3600)

if __name__ == '__main__':
    GUI.run(GUI())
