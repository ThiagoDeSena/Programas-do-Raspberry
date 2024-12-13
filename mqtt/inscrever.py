import paho.mqtt.client as mqtt
import time

mensagem_anterior = ""

def receber_mensagem(cliente,userdata,message):
    time.sleep(0.2)
    global mensagem_anterior
    nova_mensagem = str(message.payload.decode("utf-8"))
    
    if nova_mensagem != mensagem_anterior:
        print("Mensagem recebida:")
        print(f"Temperatura: {nova_mensagem} ºC")
        mensagem_anterior=nova_mensagem
    

cliente = mqtt.Client(client_id="rasp",protocol=mqtt.MQTTv311)
conexao = cliente.connect(host="10.0.0.106") 
#10.0.0.105 
#mqtt-dashboard.com

cliente.loop_start()
cliente.subscribe("room/temperature")
#cliente.subscribe("room/lamp")



while True:
    cliente.on_message=receber_mensagem
    
    