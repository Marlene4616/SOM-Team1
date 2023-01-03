from bottle import route, run, template, static_file, request, error
import datetime
#from SensorDaten import


#@route('/hallo/<name>')
#def index(name):
    #return template('<b>Hello {{name}}</b>!', name.data_to_string)

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
    return template('temperatur')

@route('/luftfeuchtigkeit')
def humidity():
    return template('luftfeuchtigkeit')

@route('/livedaten')
def livedaten():
    return template('livedaten'),'aktuelle Temperatur: 20°C', ' \n aktuelle Luftfeuchtigkeit: 80% '


run(host='localhost', port=8080, reloader=True)
