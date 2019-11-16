import paho.mqtt.client as mqtt
import time
from random import randint as rnd
# Variáveis para acesso ao servidor
user = 'c445a7a0-06e8-11ea-8221-599f77add412'
password = '88e4c973b8d8bb754f2d15ca3adbe3cab1b00899'
client_id = '0ac33d30-06eb-11ea-a4a3-7d841ff78abf'
server = 'mqtt.mydevices.com'
port = 1883

def publish(channel:str,variable,response_data:str):
    client.publish('v1/' + user + '/things/' + client_id + f'/{response_data}/{channel}', variable)

def subscribe(channel:str):
    client.subscribe('v1/' + user + '/things/' + client_id + f'/cmd/{channel}')

def sensor_t_u():
    return rnd(-12,30),rnd(0,100)

def rele(estado:int):
    if estado == 1:
        print("Rele ligado...")
    else:
        print("Rele desligado...")

def mensagem(client, userdata, msg):
    t = msg.topic.split('/')
    v = msg.payload.decode().split(',')
    rele(v[1])
    publish(2,v[0],'response')
# Cria o objeto para acessar o servidor (Client ID)
client = mqtt.Client(client_id)

# Informa ao objeto o usuário e senha para acesso ao servidor (MQTT username, MQTT password)
client.username_pw_set(user, password)

# Estabelece a conexão com o servidor (MQTT Server, MQTT Port)
client.connect(server, port)

client.on_message = mensagem

client.loop_start()

subscribe(2)

while True:
    t, u = sensor_t_u()
    publish(0, t, 'data')
    publish(1, u, 'data')
    time.sleep(11)