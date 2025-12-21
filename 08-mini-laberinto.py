# Mini Laberinto

# CLASE Habitacion:
#     ATRIBUTOS: nombre, descripcion, conexiones (diccionario de direcciones a otras habitaciones)
#     MÉTODO: mostrar_info() → imprime nombre y descripción

# CLASE Jugador:
#     ATRIBUTOS: habitacion_actual
#     MÉTODO: mover(direccion) → cambia habitacion_actual si la dirección es válida

# INICIO
#     CREAR habitaciones (ej. cocina, sala, pasillo)
#     CONECTAR habitaciones entre sí (ej. cocina["norte"] = sala)
#     CREAR jugador y colocarlo en una habitación inicial

#     MIENTRAS el jugador no escriba "salir":
#         MOSTRAR información de la habitación actual
#         PEDIR dirección al jugador
#         LLAMAR jugador.mover(direccion)
#     FIN MIENTRAS

#     MOSTRAR "Juego terminado"
# FIN



class Habitacion:
  def __init__(self, nombre, descripcion, conexiones):
    self.nombre = nombre
    self.descripcion = descripcion
    self.conexiones = conexiones
  def mostrar_info(self):
    print(f"Nombre: {self.nombre} y Descripcion: {self.descripcion}")

cocina = Habitacion("Cocina", "Una cocina con olor a pan recién horneado.", {})
sala = Habitacion("Sala", "Una sala con un sillón cómodo.", {})
pasillo = Habitacion("Pasillo", "Un pasillo largo y oscuro.", {})


cocina.conexiones["norte"] = sala
sala.conexiones["sur"] = cocina
sala.conexiones["este"] = pasillo
pasillo.conexiones["oeste"] = sala


class Jugador:
  def __init__(self, habitacion_actual):
    self.habitacion_actual = habitacion_actual
  def mover(self, direccion):
    if direccion in self.habitacion_actual.conexiones:
      self.habitacion_actual = self.habitacion_actual.conexiones[direccion]
      print(f"Te moviste hacia {direccion}")
    else:
      print("No puedes ir en esa dirección")


def juego():
    jugador = Jugador(cocina)  # Empieza en la cocina
    print("Bienvenido al laberinto. Escribe 'salir' para terminar.")

    while True:
        jugador.habitacion_actual.mostrar_info()
        direccion = input("¿A dónde quieres ir? (norte/sur/este/oeste): ").lower()
        if direccion == "salir":
            print("¡Gracias por jugar!")
            break
        jugador.mover(direccion)

juego()
