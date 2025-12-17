# Tablas de Multiplicar
# INICIO
#   PEDIR al usuario un número
#   MOSTRAR mensaje: "Tabla de multiplicar del número"
#   PARA i desde 1 hasta 10
#       resultado = número * i
#       MOSTRAR "número x i = resultado"
#   FIN PARA
# FIN

def tablas_multiplicar():
  numero = int(input("Digita un número: "))
  print(f"Tabla del número: {numero}")
  for i in range(1,11,1): # range(start,stop,step)
    resultado = numero * i
    print(f"{numero } * {i} = {resultado}")
tablas_multiplicar()