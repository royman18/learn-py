# Adivina el Número
# INICIO
#   GENERAR un número aleatorio entre 1 y 10
#   MIENTRAS el usuario no adivine
#       PEDIR un número
#       SI el número es igual al secreto
#           MOSTRAR "¡Correcto!"
#           TERMINAR
#       SI el número es mayor
#           MOSTRAR "Demasiado alto"
#       SI el número es menor
#           MOSTRAR "Demasiado bajo"
# FIN

import random

randomNum = random.randint(1,10)

def adivinanza():
  while True:
    usuario = int(input("Elige un Número del 1 al 10: "))
    if usuario > randomNum:
      print("Demasiado alto")
      break
    elif usuario < randomNum:
      print("Demaciado bajo")
    else:
      print("Correcto")
      break

adivinanza()