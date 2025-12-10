# Calculadora

num1 = int(input("Digita tu primer número: "))
ope= input("Digita tu operacion a realizar: (+,-,*,/): ")
num2 = int(input("Digita tu segundo número: "))
def calculadora(num1, ope, num2):
    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        return num1 / num2
    else:
        print("Vuelve a Ejecutar el Programa")

print("El resultado es: ", calculadora(num1,ope,num2))
