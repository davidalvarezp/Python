
#lista=[1,2,3,4,5]

#print(lista(0))

#objetos
#lista.append
#lista.insert
#lista.remove
#lista.clear
#lista.count
#lista.copy no es la original
#lista.reverse
#lista.pop L.I.F.O devuelve el valor de la pila y lo muestra, eliminandolo
#lista.index devuelve la posición(0,1,2,3)(numº a buscar,desde qué posicion,hasta qué posicion)
#lista.sort ordena la lista .sort([resverse=True],key=funcion(def))
#lista.extend(lista2) se le suma otra lista

def printlist(lista):
    for i in lista:
        print(i, end=", ")
    print()

# 1 Crea un programa que mientras el usuario no introduzca un número valido siga pidiendo entrada de datos.
def ejer1():
    numeros=[1,2,3,4,5,6,7,8,9]
    while True:
        try:
            n1=int(input("Introduce un num del 1 al 9: "))
            if n1 in numeros:
                print("bien")
                break
            else:
                print("mal")
        except ValueError:
            print("Introduce num valido")
            ejer1()

# 2 Realiza un método al cual se le pasa una lista y devuelve la suma de sus elementos.
def ejer2(lista):
    
    suma=0;
    for i in lista:
            try:
                    suma=suma+i;
            except:
                    pass
    return suma;

lista=[1,2,3,4,5]


    # for i in range (len(lista)):
    #     if lista[i]%2!=0:
    #         lista.remove(i)
    #     print(i,lista[i])
    #     lista[i]= lista[i]*2;
    # print(lista)

# 3 Crea una función que pida al usuario 5 números y los guarde en una lista y devuelva esa lista.
    # Ø Muestra la lista
    # Ø Calcula y muestra la media de los números
    # Ø A continuación, reemplaza todos los números negativos de esa lista por 0.
    # Ø Vuelve a mostrar la lista
def ejer3 (a,b,c,d,e):
    try:
        suma=0
        lista=[a,b,c,d,e]
        print(lista)
        for i in lista:
            suma=suma+i
            media=suma/5
        print(suma)
        print(media)
        for j in range(0,4):
            if lista[j]<0:
                lista[j]=0
        print(lista[:])
    except:
         print('Números no válidos')
         pass
    

# 4 A partir de una lista, escribe un programa que cree una lista nueva con los elementos de
    # la primera lista que sean impares
def ejer4 (lista):
    
    lista2=[]
    for i in lista:
        if i%2!=0:
            lista2.append(i)
    print(lista2)

# 5 Crea una función que borre los números pares de una lista pasada como parámetro.
def ejer5 (lista):

    for i in lista:
        if i%2==0:
            lista.remove(i)
    print(lista)

# 6 Escribe una función que reciba una lista de enteros y devuelva otra lista con los dobles de sus elementos
def ej6 (lista):
    
    lista2=[]
    for i in lista:
        lista2.append(i*2)
    print(lista2)

# 7 Crea una lista con los nombres de los meses del año. Solicita al usuario que introduzca un
# nombre de mes. Si el nombre se encuentra en la lista, se mostrará el número de mes. Si
# el nombre no se encuentra en la lista, se mostrará un mensaje indicando que no existe
# ese mes, y se volverá a solicitar al usuario que introduzca un nombre de mes, hasta que
# introduzca el nombre de un mes válido.
def ejer7():

    meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    num=input('dime un mes en minusculas ')
    print('el numero de tu mes es '+str(meses.index(num)+1))


# 8 Dada una lista de palabras, crea una nueva lista que contenga solo las palabras que tienen más de 5 letras.
def ejer8(lista):

    palabras=[]
    for i in lista:
        if len(i)>5:
            palabras.append(i) 
    printlist(palabras)


# 9 A partir de una lista, escribe una función que cree una lista nueva eliminando aquellos que están repetidos.
def ejer9(palabras):

    palabras_repetidas=[]
    for i in palabras:
        if palabras.count(i)>1:
            palabras_repetidas.pop(i)
    print(palabras_repetidas)


# 10 A partir de una lista con los nombres de las personas que forman un grupo, solicita al
    #usuario que introduzca un nombre y cuenta cuántas veces aparece dicho nombre en la lista.
def ejer10 (a):

    grupo=('David','Denis','Adrián','Alejandro')
    print(grupo.count(a))


# 11 Escribe una función que reciba dos listas y devuelva una tercera con los elementos comunes a ambas.
def ejer11(lista1,lista2):

    print (lista1+lista2)


# 12 Utilizando una lista, escribe una función a la que se le pase el número del mes y devuelva su nombre.
def ejer12():

    meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    a=int(input('dime un numero de mes '))
    print('el numero de tu mes es '+(meses[(a-1)]))


# 13 Busca el algoritmo para calcular la letra del DNI y crea una función que use listas para devolver la letra del mismo.
def ejer13():

    letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    a=int(input('Inserta tu número de dni:'))
    dni_final=letras_dni[(a%23)]
    print(dni_final)

# 14 Crea una función a la que se le pase un día de la semana y devuelva el siguiente, por
    # ejemplo, si le pasamos lunes nos devolverá martes y si le pasamos domingo lunes.
def ejer14():

    dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    a=input('Introduce un día de la semana:')
    b=dias.index(a)
    b=b+1
    print('El día siguiente es ' + dias[b])

# 15 Utilizando una tupla, escribe una función a la que se le pase el número del mes y devuelva su nombre.
def ejer15():

    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    a=int(input('Introduce el numero de un mes:'))
    print('El mes de tu numero es: '+(meses(a-1)))


# 16 Crea una función que devuelva la tabla de multiplicar del 0 al 10. Realiza su visualización
    # para que se muestre de forma similar a la siguiente:
def ejer16a():
    tabla = []                          #lista vacía
    numeros = [1,2,3,4,5,6,7,8,9,10]    #valores a multiplicar
    for i in numeros:
        fila = []                       #lista vacía
        for j in numeros:
            fila.append(i * j)          #añadir el resultado de la multiplicación a la fila
        tabla.append(fila)              #añadir la fila a la tabla
        
    #visualización de la tabla:
    for fila in tabla:
        for numeros in fila:
            print(numeros,end="\t")
        print()


def ejer16b():
    tabla_result = ""                   #tabla para el resultado
    numeros = [1,2,3,4,5,6,7,8,9,10]    #valores a multiplicar
    for i in numeros:
        fila = []                       #lista vacía
        for j in numeros:
            fila.append(i * j)          #añadir el resultado de la multiplicación a la fila
    for numero in fila:
        tabla_result = tabla_result + str(numero) + " "
    tabla_result = tabla_result + "\n"
    print(tabla_result)
        


def ejer16c():
    nueva_tabla=[]
    b=0
    tabla=[1,2,3,4,5,6,7,8,9,10]
    tabla
    for j in (tabla):
        nueva_tabla=[]
        for i in (tabla):
            b=j*i
            nueva_tabla.append(b)
        print(nueva_tabla)

# 17 Crea una lista bidimensional que contenga los agrupamientos del alumnado de una clase para
    #un determinado proyecto. La lista contendrá otras listas con los componentes de cada grupo.
def ejer17():
    grupos = []

    grupos.append(["Luis", "Juan"])
    grupos.append(["María", "Elba", "Mario"])
    grupos.append(["Carola"])
    grupos.append(["Pablo", "Manuel", "Raquel", "Uxía"])

    for grupo in grupos:
        
        for i in range(len(grupo)):
            if i == len(grupo) - 1:
                print(grupo[i], end="")
            else:
                print(grupo[i], end=", ")
        print()  


#-------------------------------------------#

# lista=[1,2,3,4,5]
# for i in range(len(lista)-1,-1,-1):
#      if (lista[i]%2!=0):
#         del lista[i]
# print(lista)


# suma=0
# cont=0
# num=-1

# while (num:=int(input("Num:")))!=0:
#     cont+=1
#     suma+=num
# print(f"Media {suma/cont} {suma} {cont}")



# 20 20.Crea una lista bidimensional 3x3 que sirva para jugar al tres en raya, almacenará 3
    # posibles cadenas, una cadena vacía para indicar que no se ha puesto una ficha en esa
    # posición, una 'o' para indicar que ha jugado el jugador 1 y una 'x' para el jugador 2.
        # Ø Crea una función que vacíe el tablero (rellene el tablero con cadenas vacías).
        # Ø Crea una función que borre la pantalla y visualice el tablero.
        # Ø Crea una función que la recorra y que busque si se ha producido 3 en raya para el 
        # jugador 1 en alguna de las filas.
        # Ø Crea una función que la recorra y que busque si se ha producido 3 en raya para el
        # jugador 1 en alguna de las columnas.
        # Ø Crea una función que la recorra y que busque si se ha producido 3 en raya para el
        # jugador 1 en alguna de las diagonales.
        # Ø Crea una función que la recorra y que busque si se ha producido 3 en raya para algún jugador.
        # Ø Completa el ejercicio para que dos jugadores puedan jugar al 3 en raya.

def ejer20():
    print()


def ejer20a():
    tablero = []
    tablero.append(["o", "x", "o"])
    tablero.append([" ", " ", " "])
    tablero.append([" ", " ", " "])

    print("-------")
    for casilla in tablero:
        print("|", end="")
        for i in range(len(casilla)):
            print(casilla[i], end="|")
        print("\n-------")


def ejer20b(jug):
    tablero = []
    tablero.append(["x", "o", "o"])
    tablero.append(["x", "x", "o"])
    tablero.append(["x", "x", "x"])

    win = 0

    for fila in tablero:
        cad="".join(fila)
        cad1=cad.replace(jug,"")

        if len(cad1)==0:
            win+=1
        else:
            win+=0
    if win!=0:
        print("El jugador",jug,"ha ganado")
    else:
        print("El jugador \"",jug,"\" NO ha ganado")


ejer20b("x")

def ejer20bc():

    print()

def ejer20d():
        
    print()
