import RPi.GPIO as GPIO
from pynput.keyboard import Controller, Key #controller permite usar las teclas y Key son las teclas pero especiales ( espacio, entrer, escape...)
import time

# Configuración de los pines en modo BOARD
GPIO.setmode(GPIO.BOARD)

# Diccionario: pin físico → tecla a simular
pines = {
    11: '1',
    13: '2',
    16: '3',
    18: '4',
    12: Key.space
}

# Configura cada pin como entrada con pull-up
for pin in pines:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

keyboard = Controller()

print("Sistema iniciado. Esperando botones...")

try:
    while True:
        #.items() Se para el diccionario y lo almacena en pin y tecla(Clave/Valor). Ej pin = 11 mientras tecla = 1.
        for pin, tecla in pines.items():
            if GPIO.input(pin) == GPIO.LOW:  # Pulsado
                keyboard.press(tecla)
                keyboard.release(tecla)
                print(f"Tecla '{tecla}' enviada")
                time.sleep(0.5)  # Antirrebote simple
except KeyboardInterrupt:
    print("\nPrograma terminado")
finally:
    GPIO.cleanup()
