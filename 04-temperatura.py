#Convertidor de Temperatura

# INICIO
#   MOSTRAR menú:
#     1. Convertir °C a °F
#     2. Convertir °F a °C
#   PEDIR opción al usuario
#   PEDIR temperatura

#   SI opción es 1
#       resultado = (temperatura * 9/5) + 32
#       MOSTRAR resultado en °F

#   SI opción es 2
#       resultado = (temperatura - 32) * 5/9
#       MOSTRAR resultado en °C

#   SI opción no es válida
#       MOSTRAR "Opción inválida"
# FIN


def menu():
  print("Convertidor de Temperatura\n1. Convertir °C a °F\n2. Convertir °F a °C\n")

def temp_converter():
  menu()
  opcion_usuario = int(input("Elige alguna de las dos opciones del Menú: "))
  temp_usuario = float(input("Digita la temperatura a convertir: "))
  if opcion_usuario == 1:
    resultado = (temp_usuario * 9/5) + 32
    return f"Conversión: {resultado:.2f} °F"
  elif opcion_usuario == 2:
    resultado = (temp_usuario - 32) * 5/9
    return f"Conversión: {resultado:.2f} °C"
  else:
    print("Opción inválida") 
    
print(temp_converter())