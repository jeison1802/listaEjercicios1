### 7. 

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if(num1==num2):
    print("Los numeros son iguales.")
else: 
    print("Los numeros son distintos. ")
    if(num1>num2):
        print("El primero es mayor que el segundo.")
    elif(num1<=num2):
        print("El segundo es mayor o igual que el primero.")

