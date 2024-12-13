# Bibliotecas utilizadas
import RPi.GPIO as GPIO # Para utilizar os pinos de GPIO
import time # Para usar o time.sleep
GPIO.setmode(GPIO.BOARD)
pinoLED = 12 # Vamos utilizar o pino 12 da placa
# Define o pino do LED como saída
GPIO.setup(pinoLED, GPIO.OUT)
while(1): #Repete esta secao sempre
    print("Oi")
    GPIO.output(pinoLED, True) # Acende o LED
    time.sleep(0.5) # Aguarda meio segundo
    GPIO.output(pinoLED, False) # Apaga o LED
    time.sleep(0.5) # Aguarda meio segundo