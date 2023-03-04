
### 2. Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado 

radio = int(input("Ingrese el radio: "))
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))
lado = int(input("Ingrese el lado del cuadrado: "))

pi = 3.1416
area_circulo = pi*radio**2
area_triangulo = base*altura/2
area_cuadrado = lado**2 

print(f"El area del circulo es: {area_circulo}")
print(f"El area del triangulo es: {area_triangulo}")
print(f"El area del cuadrado es: {area_cuadrado} ")