x=True #Definimos una variable booleana
fechas=[] #Definimos una lista vacia para las fechas
notas=[] #Definimos una lista vacia para las notas
while x==True: #Mientras se cumpla que x es verdadero estará corriendo el codigo en bucle
    print("1-Leer Nota\n2-Escribir Nota\n3-Eliminar Nota\n4-Salir\n")
    eleccion=int(input("¿Que desea realizar?(debe elegir un numero): ")) #VARIABLE DONDE SE GUARDA ELECCION DEL USUARIO, convertimos de variable string a int
    if eleccion <=0 or eleccion>=5 or None: #Definimos una condicional para que el usuario no ingrese un numero que sea 0 o menor o mayor o igual a 5
        print("Debe ingresar un numero entre 1 y 4")
    else:
        if eleccion == 1:
            if not fechas and not notas: #Si el array fechas y notas no contiene ningun tipo de dato dentro, arroja el mensaje siguiente
                print("\nNo existen notas en las listas para leer")
            else:
                print("Fechas:")
                for i in range(len(fechas)): #Realizamos un for que recorra un rango de longitud del tamaño del array fechas, osea recorre todo el array con todas las fechas que contenga la lista
                    print("{}{} {}".format(i+1,')', fechas[i])) #Realizamos un print con formato 1) (Fecha) mostrando todas las fechas
                eleccion_lectura=int(input("Ingrese la Nota que desea ver(debe solamente debe elegir una y un numero por ejemplo: 1, para la primera fecha): "))
                if eleccion_lectura <1 or eleccion_lectura>len(fechas):#Ponemos una condicional if para que el programa no se caiga, para que el usuario solamente ingrese valores que existan
                    print ("Debe ingresar un valor valido")
                else:
                    print("\nFecha:",fechas[(eleccion_lectura-1)],"\nNota:",notas[(eleccion_lectura-1)])#De cumplirse el rango, imprimimos el valor, el usuario al ingresar 1 y python empieza con valor 0, le restamos 1
        elif eleccion == 2:
            nota_escritura=input("Escriba la nota:\n")
            fecha_escritura=input("Escriba fecha de la nota (dd-mm-aa o dd/mm/aa):\n")
            fechas.append(fecha_escritura)#Se guarda la fecha en ultima posicion la lista 
            notas.append(nota_escritura)#Se guarda la nota en ultima posicion la lista 
        elif eleccion == 3:
            if not fechas and not notas: #Si el array fechas y notas no contiene ningun tipo de dato dentro, arroja el mensaje siguiente
                print("\nNo existen notas en las listas para poder eliminar")
            else:
                print("Fechas:")
                for i in range(len(fechas)):#Realizamos un for que recorra un rango de longitud del tamaño del array fechas, osea recorre todo el array con todas las fechas que contenga la lista
                    print((i+1),fechas[i])
                eleccion_eliminacion=int(input("Ingrese la Nota que desea eliminar (debe solamente debe elegir una y un numero por ejemplo: 1, para la primera fecha):"))
                if eleccion_eliminacion <1 or eleccion_eliminacion>len(fechas):#Ponemos una condicional if para que el programa no se caiga, para que el usuario solamente ingrese valores que existan
                    print ("Debe ingresar un valor valido")
                else:
                    fechas.pop((eleccion_eliminacion-1)) #Eliminamos el elemento dada la posicion dada por el usuario
                    notas.pop((eleccion_eliminacion-1)) #Eliminamos el elemento dada la posicion dada por el usuario
        elif eleccion == 4:
            x=False #Si el usuario elige salir, x será falso, entonces hará un quiebre en el bucle while y se saldrá
            print("Vuelva Pronto...")