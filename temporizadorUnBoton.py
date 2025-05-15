#Modulo para leer los pines 
import RPi.GPIO as GPIO
#Libreria para simular entradsa del teclado o mouse en entorno grafico
from pynput.keyboard import Controller, Key 
# Libreria para pausar programa un momento
import time

# Configuración del pin
GPIO.setmode(GPIO.BOARD) #GPIO.BOARD es el modo que se identifica los pines esta BCM o Board

# Se define PIN
PULSADOR = 11

#Se configura Pulsador como entrada(GPIO.IN), se configura el pin como HIGH. 
GPIO.setup(PULSADOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Controlador del teclado
keyboard = Controller()

print("Esperando pulsador...")

#Se espera ...
try:
    while True:
        # Se compara si el pulsador esta presionado(LOW)
        if GPIO.input(PULSADOR) == GPIO.LOW:
            #Presiona el 1 y luego lo suelta
            keyboard.press('1')
            keyboard.release('1')
            print("Tecla 1 enviada")
            time.sleep(0.5)
            
#Captura el error
except KeyboardInterrupt:
    print("\nPrograma terminado")
    
#El programa finaliza limpiando el pulsador(De nuevo estado High) y vuelve al While.    
finally:
    GPIO.cleanup()
