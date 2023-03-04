### 10. Defina un diccionario que tenga las siguientes llaves (nombre del curso, de alumnos, activo(tipo booleano), 
    # nombre del profesor, max. nota, alumnos(lista)) a todos ellos como valor que lleven un valor de inicialización, 
    # por ejemplo si es entero 0, si es string una cadena. 

diccionario = {'nombre_del_curso':"", 'cantidad_alumnos':0, 'activo':False, 'nombre_profesor':"", 'max_nota':0, 'alumnos':[]}
pregunta = True
cont = 0
n = 0
while(pregunta == True):
  diccionario['nombre_del_curso'] = input("Ingrese el nombre del curso ")
  diccionario['cantidad_alumnos'] = int(input("Ingrese la cantidad de alumnos"))
  diccionario['activo'] = bool(int(input("Ingrese si es activo (1)  o no activo (0)")))
  diccionario['nombre_profesor'] = input("Ingrese el nombre del profesor: ")
  diccionario['max_nota'] = int(input("Ingrese la maxima nota: "))

  while(diccionario['cantidad_alumnos']>n):
    alumno = input("Ingrese el alumno: ")
    diccionario['alumnos'].append(alumno)
    n+=1
  cont +=1
  

  print(diccionario)
  diccionario['alumnos'] = []
  n = 0
  if(cont==3):
    pregunta = bool(int(input("Desea continuar? (Sí:1) (No:0)")))
