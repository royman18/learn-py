# Movimiento en una Cuadricula

# INICIO
#   DEFINIR posición inicial del jugador (x = 0, y = 0)
#   MOSTRAR instrucciones: usar "arriba", "abajo", "izquierda", "derecha" para moverse
#   MIENTRAS el usuario no escriba "salir"
#       MOSTRAR posición actual
#       PEDIR dirección al usuario
#       SI dirección es "arriba"
#           y = y + 1
#       SI dirección es "abajo"
#           y = y - 1
#       SI dirección es "derecha"
#           x = x + 1
#       SI dirección es "izquierda"
#           x = x - 1
#       SI dirección no es válida
#           MOSTRAR "Dirección no válida"
#   FIN MIENTRAS
#   MOSTRAR "Juego terminado"
# FIN


posicion_usuario = {
  "y":0,
  "x":0
}

def movimineto():
  while True:
    print('Usar "arriba", "abajo", "izquierda", "derecha" para moverse o "salir" para terminar el juego')
    print(f"Posición actual: {posicion_usuario}")
    nueva_posicion = input(": ").lower()
    if nueva_posicion == "arriba":
      posicion_usuario["y"] +=1
    elif nueva_posicion =="abajo":
      posicion_usuario["y"] -=1
    elif nueva_posicion == "derecha":
      posicion_usuario["x"] +=1
    elif nueva_posicion == "izquierda":
      posicion_usuario["x"] -=1
    elif nueva_posicion == "salir":
      print("Juego Terminado")
      break
  
    
movimineto()
