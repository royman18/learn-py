# Contador de Pasos

# CLASE Caminante:
#     MÉTODO __init__(self, nombre):
#         - Guardar el nombre del caminante
#         - Inicializar pasos en 0

#     MÉTODO caminar(self):
#         - Aumentar en 1 el contador de pasos

#     MÉTODO mostrar_pasos(self):
#         - Mostrar cuántos pasos ha dado el caminante

# INICIO DEL PROGRAMA:
#     - Pedir al usuario su nombre
#     - Crear una instancia de Caminante con ese nombre

#     MIENTRAS el usuario quiera seguir caminando:
#         - Preguntar: "¿Quieres dar un paso? (s/n)"
#         - Si responde "s":
#             - Llamar al método caminar()
#             - Llamar al método mostrar_pasos()
#         - Si responde "n":
#             - Mostrar despedida
#             - Salir del bucle
#         - Si responde otra cosa:
#             - Mostrar "Opción no válida"
# FIN

class Caminante:
  def __init__(self, nombre, pasos = 0):
    self.nombre = nombre
    self.pasos = pasos
  def caminar(self):
    self.pasos += 1
  def mostrar_pasos(self):
    print(f"Pasos dados: {self.pasos}")  
def contador_pasos():
  nombre_usuario = input("¿Cúal es tu nombre?: ")
  nuevo_caminante = Caminante(nombre_usuario)
  while True:
    respuesta = input("¿Quieres dar un paso? (s/n): ").lower()
    if respuesta == "s":
      nuevo_caminante.caminar()
      nuevo_caminante.mostrar_pasos()
    elif respuesta == "n":
      print("Hasta pronto")
      break
    else:
      print("Opcion no válida")

contador_pasos()