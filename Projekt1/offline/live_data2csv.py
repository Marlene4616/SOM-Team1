#!/usr/bin/env python3
from paho.mqtt import client as mqtt_client
import socket
import os, time, numpy as np
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS
import pygal #, influxdb_client
from selenium import webdriver
from Offline_GUI import gui_python
from threading import Thread

class sub_data_save(object):
    """The goal of this class is to receive, edit and save data from a temperature sensor"""

    def __init__(self):
        """Declare some variables"""
        #switchs
        self.cloud_switch = False
        self.csv_switch = True
        self.live_plot = True

        #MQTT data
        self.user = socket.gethostname()
        self.MQTT_PORT = 1883
        self.MQTT_ADDRESS = "141.22.194.198"
        self.MQTT_CLIENT_NAME = f"{self.user}_PiSub"
        self.MQTT_TOPIC = "SK/Sens_Data"
        self.TICK_RATE_HZ = 5
        self.TICK_RATE = 1/self.TICK_RATE_HZ

        #Save Data
        self.csv = 'Data.csv'


        #Liste für die Nachrichten
        self.message_queue = []
        self.temp = 0.0
        self.hum = 0.0
        self.time = ""
        self.value_queue = []
      #cloud
        # self.token = "Ij77kTnnPYGiFEaTRkKK9fenS-ZYXhl0oKQXw7vO80lbCaQpayqptKyJcbNX8Cm9IsQ-3jH0VhEpS1wStsxZJQ==" #upblGiLSR7UrPeN3dtaVlil61Wnc5qTRfhXzo83IL9bqcM9GcvrselRIsRwmgDboqrGLpa7FeU9WkXUzsdvvTw==
        # self.org = "franciacohoyosgarciak@gmail.com"
        # self.url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
        #
        # self.client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.org)
        # self.bucket = "test"
        # self.write_api = self.client.write_api(write_options=SYNCHRONOUS)


        #live gauge
        self.counter = 0
        self.driver = webdriver.Edge()
        #sart
        self.verbindung()
    #Funktion die beim eintreffen einer Nachricht diese in eine Liste packt
    def on_message(self, client, userdata, msg):

        message = msg.payload.decode()

        self.message_queue.append(message)

    def verbindung(self):
        ''' Verbinden mit MQTT'''
        #
        client = mqtt_client.Client(self.MQTT_CLIENT_NAME)
        client.connect(self.MQTT_ADDRESS, self.MQTT_PORT)
        #Subscribe zum Thema und Funktion "on_message" hinzufügen
        client.subscribe(self.MQTT_TOPIC)
        client.on_message = self.on_message
        #Für immer laufen lassen
        client.loop_start()
    def data_saver(self,RAW_data):
        '''depending on which switch is on, a .csv will be created, the data will be sent to the cloud or only the processed data will be returned'''

        data = RAW_data.replace("temp: ", "").replace("hum: ", ",").replace("time: ", ",")
        if self.csv_switch == True and 'None' not in data:
            if os.path.exists(self.csv) == False:
                _ = "x"
                with open(self.csv, _) as csv:
                    csv.write('Temperatur,Feuchtigkeit,Datetime\n')
            _ = "a"
            with open(self.csv, _) as csv:
                csv.write(f"{data}\n")
        data = data.split(",")
        return float(data[0]), float(data[1]), str(data[2])
    # def cloud_add(self):
    #     '''This function sends the data to a cloud where you can continue working and be independent of the VPN of the University'''
    #
    #     if self.cloud_switch == True:
    #         point1 = (
    #             Point("Temperature")
    #             .field("T:", self.temp)
    #         )
    #         self.write_api.write(bucket=self.bucket, org="franciacohoyosgarciak@gmail.com", record=point1)
    #
    #         point2 = (
    #             Point("Humidity")
    #             .field("H:", self.hum)
    #         )
    #         self.write_api.write(bucket=self.bucket, org="franciacohoyosgarciak@gmail.com", record=point2)

    def live_gauge(self):
        '''with this function an SVG is generated that shows the current values of the sensors'''
        gauge = pygal.Gauge()
        gauge.title = 'SOM Live Gauge'

        gauge.range = [-10, 50, 30]
        gauge.add('Temp [C°]: ', self.temp)
        gauge.add('Hum [%]: ', self.hum)

        gauge.render_to_file('file.svg')

        url = os.getcwd() + "\\file.svg"
        if self.counter == 0:

            self.driver.get(url)
            self.counter = 1
        else:
            self.driver.refresh()

        time.sleep(3)
    #     os.remove(url)
    def run(self):
        thread_1 = Thread(target=gui_python, daemon=True)
        thread_1.start()
        print("Thread 1")


if __name__ == '__main__':
    start = sub_data_save()
    a = True
    while True:

        last_value = ""

        # Kurz warten
        time.sleep(start.TICK_RATE)
        # Wenn es noch neue Nachrichten gibt...
        while len(start.message_queue) > 0:
            # ...dann kopiere diese von der Empfangsliste in die Anzeige-Liste
            last_value = start.message_queue.pop()

            start.temp, start.hum, start.time = start.data_saver(last_value)

            # start.cloud_add()
            start.live_gauge()
            if len(last_value) > 10:
                start.value_queue.append(last_value)
            if a == True:
                start.run()
                a = False

            print(last_value)