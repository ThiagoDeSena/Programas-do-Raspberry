import time
time.sleep(3) 

import paho.mqtt.client as mqtt
import mariadb
import sys
import datetime


try:
    conecao = mariadb.connect(
        user="user01",  #usuário criado no mariaDB
        password="pi",  #Senha Criada no mariaDB para o usuário 'user01'
        host="localhost",
        database="temperatura_e_humidade"    #Nome do banco de teste criado no mariaDB
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)

def inserir_valores(temperatura,umidade):
    cursor.execute("INSERT INTO valores (temperatura,umidade) VALUES (?,?)",(temperatura,umidade)) ##Insere os valores de "temperatura" e "umidade" na tabela 'valores' do banco de dados

cursor = conecao.cursor()
dados ={"temperature":None,"humidity":None,"lamp":None}
ultima_temperatura = 0
ultima_umidade = 0
ultima_insercao = time.time()   #Hora atual

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
        tempo = datetime.datetime.now()
        print(f"Temperatura: {dados['temperature']} ºC , Humidade: {dados['humidity']}%, Lampada: {dados['lamp']},  Data: {tempo}")

        global ultima_temperatura
        global ultima_umidade
        global ultima_insercao

        if ultima_temperatura != dados["temperature"] or ultima_umidade!=dados["humidity"] or time.time() - ultima_insercao >=300:
            inserir_valores(dados['temperature'],dados['humidity'])
            conecao.commit() ##Salva as alterações feitas no banco de dados
            ultima_temperatura = dados["temperature"]
            ultima_umidade = dados["humidity"]
            ultima_insercao = time.time()   #Recebe a hora atual em que foi inserido valores no banco

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


print(f"Last Inserted ID: {cursor.lastrowid}")
cursor.close()
conecao.close()

while True:
    pass

   