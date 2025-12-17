# Simulador de dados

# INICIO
#   MOSTRAR mensaje: "Simulador de dados"
#   MIENTRAS el usuario quiera seguir jugando
#       GENERAR un número aleatorio entre 1 y 6
#       MOSTRAR el resultado del dado
#       PREGUNTAR al usuario si quiere lanzar de nuevo (s/n)
#       SI elige "n"
#           SALIR del bucle
#   FIN MIENTRAS
# FIN
import random
def simulador_dados():
  print("*** Simulador de Dados ***")
  while True:
    random_num = random.randrange(1,7)
    print(f"🎲 Resultado: {random_num}")
    user = input("¿Quieres lanzar los dados de nuevo? (Enter/n): ").lower()
    if user == "n":
      print("Hasta Pronto")
      break
    else:
      print("Entrada no valida. Intenta con 's' o 'n'. ")
simulador_dados()