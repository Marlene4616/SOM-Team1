# This class reads the sensor data from the DHT11, sends it to a mqtt server and save the Data into a csv file
from datetime import datetime as date
from paho.mqtt import client as mqtt_client
import Adafruit_DHT,os, time
from threading import Thread

class SensorDaten:
    def __init__(self):
        # mqtt properties
        self.mqtt_switch=True
        self.mqtt_user = "Group1_send"
        self.mqtt_port = 1883
        self.mqtt_adress = "141.22.194.198"
        self.mqtt_topic = "SK/Sens_Data"
        self.freq_mqtt = 2  # [s]

        # sensor properties
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 4

        # data save properties
        self.csv_switch=True
        self.csv = 'Data.csv'
        self.freq_csv = 10 * 60  # [s]

        # data properties
        self.hum, self.temp = self.receive_data()
        self.time = self.receive_time()
        self.data_string = self.data_to_string()

    def receive_data(self):
        return Adafruit_DHT.read_retry(self.sensor, self.pin)

    def receive_time(self):
        return date.now()

    def data_to_string(self):
        time_short=self.time.strftime("%d.%m.%Y  %H:%M:%S")
        return f"temp: {self.temp}hum: {self.hum}time: {time_short}"

    def publisher(self):
        if self.mqtt_switch == True:
            client = mqtt_client.Client(self.mqtt_user)
            client.connect(self.mqtt_adress, self.mqtt_port)
            while True:
                self.hum, self.temp = self.receive_data()
                if type(self.temp) == 'float' or self.hum<100 :
                    self.time = self.receive_time()
                    self.data_string = self.data_to_string()

                    client.publish(self.mqtt_topic, self.data_string)

                    time.sleep(self.freq_mqtt)
                else:
                    time.sleep(self.freq_mqtt)


    def data_saver(self):
        while True:
            self.hum, self.temp = self.receive_data()
            if type(self.temp) == 'float' or self.hum<100 :
                self.time = self.receive_time()
                '''depending on which switch is on, a .csv will be created, the data will be sent to the cloud or only the processed data will be returned'''

                data = f'{self.temp},{self.hum},{self.time}'
                if self.csv_switch == True:
                    if os.path.exists(self.csv) == False:

                        _ = "x"
                        with open(self.csv, _) as csv:
                            csv.write('Temperatur,Feuchtigkeit,Datetime\n')
                    _ = "a"
                    with open(self.csv, _) as csv:
                        csv.write(f"{data}\n")

                time.sleep(self.freq_csv)

            else:
                time.sleep(self.freq_csv)
    def run(self):
        print("SensorDaten is active")
        thread_2 = Thread(target=self.data_saver, daemon=True)
        thread_1 = Thread(target=self.publisher, daemon=True)
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
        print("SensorDaten is closed")

if __name__ == '__main__':
    start = SensorDaten()
    start.run()

