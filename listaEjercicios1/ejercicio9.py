
### 9. Defina una lista con al menos 4 elementos que a su vez sean tuplas que tengan la siguiente estructura ('nombre','edad','dni')
#   y otra que sea una lista de dnis. 

#  - Realizar un programa que filtre a la persona de mayores de edad y a los que cumplen esa opción verificar que su dni se 
    # encuentre ahí, por último imprimir el nombre de las personas que cumplen las condiciones anteriores. 

#  - 

lista = [("Jeison",20,"72403104"),("Arturo",8,"21233455"),("Daysi",58,""), ["12345678","98765432","45678901"]]
lista_vacia = []

i = 0
print("Los usuarios que cumplen las condiciones son:")
while(i<3):
        
  if((lista[i][1])>=18):
       
        if(bool(lista[i][2]) ==  True):
            print(lista[i][0])
            lista_vacia.append(lista[i][0])
        
  i = i + 1

print('La nueva lista es: ',lista_vacia)

