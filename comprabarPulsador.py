import RPi.GPIO as GPIO
import time

# Usar numeración BCM (GPIO)
GPIO.setmode(GPIO.BCM)

# Definir el pin
PULSADOR = 17

# Configurar el pin como entrada con resistencia pull-up interna
GPIO.setup(PULSADOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Esperando pulsador... (Ctrl+C para salir)")

try:
    while True:
        if GPIO.input(PULSADOR) == GPIO.LOW:  # Pulsado (porque usa pull-up)
            print("1")
            time.sleep(0.3)  # Pequeño delay para evitar rebote
except KeyboardInterrupt:
    print("\nPrograma terminado")
finally:
    GPIO.cleanup()
