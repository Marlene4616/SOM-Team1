# Raspberry PI und Sensordaten

## Inhalt
1. [Allgemeine Informationen](#allgemeine-informationen)
2. [Anforderungen](#anforderungen)
3. [Installation](#installation)
4. [Bedienung](#bedienung)

***
## Allgemeine Informationen 
>SensorDaten ist ein Programm zur Messung und Darstellung von Temperatur und Luftfeuchtigkeit über die Zeit, welche über 
einen Raspberry Pi mit entsprechendem Sensor ermittelt werden.
Über die Web-GUI "GUI.py" werden Livedaten, Diagramme von Temperatur und Luftfeuchtigkeit und die csv-Datei als Download herausgegeben. 
Über die Python-GUI "Offline_GUI.py" wird ein Diagramm der Temperatur, die über die csv-Datei erstellt angezeigt,
sowie die durchschnittliche Temperatur und Luftfeuchtigkeit ermittelt. Über einen Button ist die Web-Gui verlinkt.
>
>Das Programm ist aus folgenden Dateien zusammengesetzt:
>* SensorDaten.py
>* Offline_GUI.py
>* GUI.py
>
>Die Formatierung der Web-Gui wird durch die folgenden Templates realisiert:
>* menu.tpl
>* downloads.tpl
>* temperatur.tpl
>* livedaten.tpl
>* luftfeuchtigkeit.tpl
>
>Zum Aufrufen der WebGui, bitte [hier](http://141.22.36.123:8080/) klicken.
***

## Anforderungen
>
>* Python 3, z.B. PyCharm Community
>* Gitlab
>* Raspberry Pi (getestet mit Raspberry Pi)
>* [DHT11 basic temperature-humidity sensor](https://www.adafruit.com/product/386)
>* PuTTy (zum remote Programmieren, Testen und Aufspielen der Programme auf den Raspberry Pi) 
>* MQTT Explorer (zum Testen und für die Kommunikation zwischen dem Raspberry Pi und der Python GUI)
>* Über VPN mit Cisco AnyConnect _ODER_ in der HAW mit dem  Internet verbunden sein
>* Browser, Zugang zum Internet

***

## Installation

>Verwende den package manager [pip](https://pip.pypa.io/en/stable/) um folgende Bibliotheken zu installieren.
Alle Bibliotheken müssen auf dem Raspberry Pi installiert werden.
>
>Pandas ist zur Verarbeitung, Analyse und Darstellung von Daten.
>
>Diese Bibliothek muss zusätzlich auf dem Computer installiert werden, um die "Offline_GUI.py" aufrufen zu können.
>```bash
>pip install pandas
>```
>Zum Verteilen der Prozesszeit auf die einzelnen Threads im Prozess
>```bash
>pip install threading
>```
>Für die Ausgabe der Zeit im Zeitstempel
>```bash
>pip install datetime
>```
>zum Senden und Empfangen der Daten über MQTT, kann zum Testen auch auf dem Computer installiert werden.
>```bash
>pip install paho.mqtt
>```
>Um die Plots für die WebGui zu erstellen
>```bash
>pip install plotly.express
>```
>um die WebGui im Browser ansteuern zu können
>```bash
>pip install bottle
>```
>Adafruit kann _NUR_ auf dem Raspberry Pi installiert werden
>```bash
>git install Adafruit_DHT
>```
>
>Der Sensor wird an Pin 4 angeschlossen.

***
## Bedienung
> ### Installation des Programmes auf dem Raspberry Pi
>* Mit dem Cisco AnyConnect verbinden oder in der Hochschule mit dem Internet verbunden sein.
>* PuTTy öffnen und mit dem Raspberry Pi verbinden:
>
>* die IP-Adresse des Raspberry Pi eingeben: 141.22.36.123 und bestätigen
>
>* Im PuTTY das Password: _raspberry_ eingeben und Enter drücken.
>
>
>```bash
>cd som-gruppe_5/Projekt1
>```
>```bash
>git pull
>```
>* abc-Kennung und Passwort eingeben
>
>* stoppen des laufenden Programmes
>```bash
>pkill -9 -f GUI.py
>```
>* Testen ob Web-GUI noch ausgeführt wird
>```bash
>ps -ef|grep GUI.py
>```
>* Starten der Web-GUI
>```bash
>nohup python GUI.py
>```

> ### Web-GUI
> 
>Aufrufen der [Web-GUI](http://141.22.36.123:8080/)
> 
> Die Navigation zwischen den Einträgen ist über das Menü möglich.
> Zum Beispiel ist die Anzeige der Temperatur, Luftfeuchtigkeit oder Download der gesammelten Messwerte als .csv Datei möglich.

> ### GUI
> Ausführen der "Offline_GUI.py"