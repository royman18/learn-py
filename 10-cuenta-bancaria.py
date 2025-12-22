# Cuenta bancaria

# CLASE CuentaBancaria:
#     MÉTODO __init__(self, titular):
#         - Guardar el nombre del titular
#         - Inicializar saldo en 0

#     MÉTODO depositar(self, monto):
#         - Sumar monto al saldo

#     MÉTODO retirar(self, monto):
#         - Si hay suficiente saldo, restar monto
#         - Si no, mostrar "Fondos insuficientes"

#     MÉTODO mostrar_saldo(self):
#         - Mostrar el saldo actual

# INICIO DEL PROGRAMA:
#     - Pedir nombre del titular
#     - Crear una cuenta bancaria

#     MIENTRAS el usuario no escriba "salir":
#         - Mostrar opciones: depositar, retirar, ver saldo, salir
#         - Según la opción:
#             - Pedir monto si aplica
#             - Llamar al método correspondiente
# FIN

class CuentaBancaria():
  def __init__(self, titular, saldo = 0):
    self.titular = titular
    self.saldo = saldo
  def depositar(self, monto):
    self.saldo += monto
    print(f"***{self.titular}, su saldo es de: {self.saldo}***")
  def retirar(self, monto):
    if monto <= self.saldo:
      self.saldo -= monto
      print(f"***Si hay suficiente saldo: {self.saldo}***")
    else:
      print("Fondos insuficientes")
  def mostrar_saldo(self):
    print(f"***{self.titular}, su saldo es de: {self.saldo}***")

def cajero_automatico():
  nombre_titular = input("Nombre del titular: ")
  nueva_cuenta = CuentaBancaria(nombre_titular)
  while True:
    opcion_usuario = int(input("Bienvenido al Banco\n*Seleccione una opción del Menú*\n1.depositar\n2.retirar\n3.ver saldo\n4.salir\n>:"))
    if opcion_usuario == 1:
      monto = float(input("-¿Cuánto deseas depositar?: "))
      nueva_cuenta.depositar(monto)
    elif opcion_usuario == 2:
      monto = float(input("-¿Cuánto deseas retirar?: "))
      nueva_cuenta.retirar(monto)
    elif opcion_usuario == 3:
      nueva_cuenta.mostrar_saldo()
    elif opcion_usuario == 4:
      print("-Gracias por usar el banco. ¡Hasta luego!")
      break
    else:
      print("-Opción no válida. Intenta de nuevo.")
      
cajero_automatico()