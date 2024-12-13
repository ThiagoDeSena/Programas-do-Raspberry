import paho.mqtt.client as mqtt
import time

def receber_mensagem(cliente,userdata,message):
    time.sleep(1)
    print("Mensagem recebida:")
    print(str(message.payload.decode("utf-8")))

cliente = mqtt.Client(client_id="rasp",protocol=mqtt.MQTTv311)
conexao = cliente.connect(host="10.0.0.105")

cliente.loop_start()
cliente.subscribe("room/temperature")

while True:
    cliente.on_message=receber_mensagem