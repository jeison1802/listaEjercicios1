
### 8. Escribir un programa que almacene la cadena de caracteres *contraseña* en una variable, pregunte el usuario 
#      por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
#      en la variable sin tener en cuenta mayúsculas y minúsculas. 

cont = "contraseña"
c = input("Ingrese la contraseña: ")

if c == cont:
    print("Coincide con la variable guardada")
else: 
    print("No coincide con la variable guardada")
