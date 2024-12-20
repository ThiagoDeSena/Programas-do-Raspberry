import paho.mqtt.client as mqtt
import time

dados ={"temperature":None,"humidity":None,"lamp":None}

def receber_mensagem(cliente,userdata,message):
    topico = message.topic #Valor do tópico que o raspberry se inscreveu
    valor = str(message.payload.decode("utf-8"))
    
    if topico == "room/temperature":
        dados["temperature"] = valor
    elif topico == "room/humidity":
        dados["humidity"] = valor
    elif topico == "room/lamp":
        dados["lamp"] = valor
    
    if dados["temperature"] is not None and dados["humidity"] is not None:
        print(f"Temperatura: {dados['temperature']} ºC , Humidade: {dados['humidity']}%, Lampada: {dados['lamp']}")
        
    

cliente = mqtt.Client(client_id="rasp",protocol=mqtt.MQTTv311)
conexao = cliente.connect(host="10.0.0.106") 
#10.0.0.105 
#mqtt-dashboard.com

#cliente.loop_start()
cliente.subscribe("room/temperature")
cliente.subscribe("room/humidity")
cliente.subscribe("room/lamp")

cliente.on_message = receber_mensagem
cliente.loop_forever()

while True:
    pass