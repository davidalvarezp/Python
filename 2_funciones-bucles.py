################################################################
def ejer1():
    u_numero=int(input("Introduce un número: "))
    if u_numero%2 == 0:
        print(f"El número {u_numero} es par")
    else:
        print(f"El número {u_numero} es impar")

################################################################
def ejer2():
    u_num1=int(input("Introduce un número: "))
    u_num2=int(input("Introduce otro número: "))
    if u_num1 < u_num2:
        print(f"{u_num1} es menor que {u_num2}")
    elif u_num2 < u_num1:
        print(f"{u_num2} es menor que {u_num1}")
    else:
        print(f"{u_num1} es igual que {u_num2}")

################################################################
def ejer3():
    v_num1=int(input("Introduce un número: "))
    v_num2=int(input("Introduce otro número: "))
    v_switch=v_num1
    v_num1=v_num2
    v_num2=v_switch
    print(f"La variable uno contiene {v_num1} y la variable dos contiene {v_num2}")

################################################################
def ejer3b():
    v_num1=int(input("Introduce un número: "))
    v_num2=int(input("Introduce otro número: "))
    v_num1,v_num2=v_num2,v_num1
    print(f"La variable uno contiene {v_num1} y la variable dos contiene {v_num2}")

###############################################################
def ejer4():
    u_num1=int(input("Introduce un número: "))
    if u_num1 < 0:
        print(f"El número {u_num1} es negativo")
    else:
        print(f"El número {u_num1} es positivo")

###############################################################
def ejer5():
    u_num1=int(input("Introduce un número: "))
    u_num2=int(input("Introduce otro número: "))
    u_num3=int(input("Introduce otro número: "))
    if u_num1 > u_num2:
        if u_num1 > u_num3:
            print(f"El número más grande es {u_num1}")
        else:
            print(f"El número más grande es {u_num3}")
    else:
        if u_num2 > u_num3:
            print(f"El número más grande es {u_num2}")
        else:
            print(f"El número más grande es {u_num3}")

###############################################################
def ejer6():
    u_num1=int(input("Introduce la temperatura en ºC: "))
    e_temp=int(input("¿A qué valor quieres pasar la temperatura?\n1-Farenheit\n2-Kelvin\n==============\n(1/2): "))
    if e_temp == 1:
        print("La temperatura en º Farenheit es",u_num1*1.8+32)
    else:
        print("La temperatura en º Kelvin es",u_num1+273)

###############################################################
def ejer7():
    v_nota=float(input("Introduce la nota del alumno: "))
    if v_nota < 0 or v_nota > 10:
        print("El valor no puede ser menor a 0 o mayor a 10, no seas malo.")
    elif v_nota < 5:
        print(f"El alumno está suspenso con la nota {v_nota}.")
    elif v_nota < 6:
        print(f"El alumno está aprobado con la nota {v_nota}.")
    elif v_nota < 7:
        print(f"El alumno está aprobado con un Bien y su nota es: {v_nota}.")
    elif v_nota < 9:
        print(f"El alumno está aprobado con un Notable y su nota es: {v_nota}.")
    elif v_nota <= 10:
        print(f"El alumno está aprobado con un Sobresaliente y su nota es: {v_nota}.")

##################################################################
def ejer7b(v_nota):
    if v_nota < 0 or v_nota > 10:
        print("El valor no puede ser menor a 0 o mayor a 10, no seas malo.")
    elif v_nota < 5:
        print(f"El alumno está suspenso con la nota {v_nota}.")
    elif v_nota < 6:
        print(f"El alumno está aprobado con la nota {v_nota}.")
    elif v_nota < 7:
        print(f"El alumno está aprobado con un Bien y su nota es: {v_nota}.")
    elif v_nota < 9:
        print(f"El alumno está aprobado con un Notable y su nota es: {v_nota}.")
    elif v_nota <= 10:
        print(f"El alumno está aprobado con un Sobresaliente y su nota es: {v_nota}.")

def ejer_8(): # 8. Realiza un programa con un bucle for que muestre los números pares entre 1 y
    # un valor pasado como parámetro..

    rango=int(input("Escribe el número del fin "))
    for i in range(1,rango):
        if i%2==0:
            print(i)

def ejer_9(): # 9. Crea un programa en Python que muestre los números desde un número mayor
    # hasta otro menor introducidos por teclado. Comprueba que el primer número es
    # mayor que el segundo, y si no lo es, muestra un mensaje y finaliza el programa.

    mayor=int(input('Ingresa el número mayor: '))
    menor=int(input('Ingresa el número menor: '))
    if mayor<menor:
        print('Números mal introducidos')
    else:
        for i in range(mayor, menor, -1):
            print(i)

def ejer_10(): # 10.Crea un programa que verifique que la contraseña introducida sea correcta. Para
    # ello pide al usuario una contraseña y almacénala. Luego, utilizando un bucle, ve
    # pidiendo la contraseña hasta que coincida con la almacenada. Muestra el número
    # de intentos realizados.
    
    password=input('Introduce tu contraseña: ')
    pass_check=input('Confirma tu contraseña: ')
    contador=int(0)
    while password!=pass_check:
        pass_check=input('Contraseña incorrecta, vuelve a intentarlo: ')
        contador=contador+1
    print('Contrseña correcta, has realizado', contador, 'intentos.')
    
def ejer_11(): # 11. Implementa un programa que muestre continuamente este menú hasta que el
    # usuario elija la opción de salir:
    #  1. Saludar
    #  2. Despedir
    #  3. Salir
    # Si el usuario elige "Saludar", el programa escribirá "Hola"; si elige "Despedir",
    # escribirá "Adiós". En ambos casos el programa continua.
    # Si elige "Salir", se detendrá la ejecución del programa.

    print('1. Saludar \n2. Despedir \n3. Salir')
    sel=int(input('Selecciona una opción: '))
    while sel!=3:
        if sel==1:
            print('Hola \n')
            sel=int(input('Selecciona una opción: '))
        elif sel==2:
            print('Adiós \n')
            sel=int(input('Selecciona una opción: '))

def ejer_12(): # 12.Realizar un programa que calcule la media de una serie de números introducidos
    # por teclado. Cuando el usuario introduzca un 0 se ha de mostrar resultado por
    # pantalla y permitir que el programa continúe para calcular una nueva media.

    suma=0
    contador=0
    num1=int(input('Insertar un número:'))
    suma=num1
    num2=1
    
    while num2!=0:
        num2=int(input('Presionar 0 para ver la media o insertar otro número:'))
        suma=suma+num2
        contador=contador+1
        
    if num2==0:
        print('La media de esos números es:',suma/contador)
        sel=int(input('Presiona 0 para salir o 1 para seguir calculando medias: '))
        if sel==0:
            print('Bye')
        elif sel==1:
            ejer_12()
    
    
    # # # num1=int(input('Insertar un número:'))
    # # # suma=num1
    # # # num1=-1
    # # contador=0
    # # sal=False
    # # while not sal:
    # #     suma=0
    # #     num2=1
    # #     while num2!=0:
    # #         num2=int(input('Presionar 0 para ver la media o insertar otro número:'))
    # #         suma=suma+num2
    # #         contador=contador+1

    # #     if num2==0:
    # #         print('La media de esos números es:',suma/contador)
    # #         sel=int(input('Presiona 0 para salir o 1 para seguir calculando medias: '))
    # #         # if sel==0:
    # #         #     print('Bye')
    # #         # elif sel==1:
    # #         #     ejer_12()
    # #     sel=int(input('Presiona 0 para salir o 1 para seguir calculando medias: '))


    
def ejer_13(num_max): # 13.Queremos escribir un programa que permita encontrar el primer valor donde la
    # suma de una secuencia supere una cantidad. Por ejemplo la suma 1+2+3+...+N
    # supera un parámetro. Si el parámetro es 2000 la solución será 63.

    suma=0
    for num in range(1,1000):
        suma=suma+num
        if suma>=num_max:
            print('El resultado es:',num)
            break

    #ejer_13(2000)
    
def ejer_14(): #Realizar un programa que calcule el factorial de un número introducido por el usuario
    # Ø Con un bucle for.
    # Ø Con un bucle while
    # Nota: El factorial de un número es el número multiplicado por todos sus
    # anteriores.
    # Como por ejemplo el factorial de 5: 5!= 5*4*3*2*1.

    def ejer_14_1(factor):
        result=1
        for i in range(1,factor+1):
            result= i*result
        print(result)
        
    def ejer_14_2(factor):
        result=1
        cont=0
        while cont < factor:
            cont+=1
            result*=cont
        print(result)
    
def ejer_15(): #Realizar un programa que saque los siguientes datos por pantalla (usa bucles for
    # y haz en un único programa todos los apartados).
    # a) Los números del 1 al 50.
    # b) En orden inversa del 50 al 1
    # c) Los números pares menores que 20 por orden creciente (2, 4, 6, ... 16, 18)
    # d) Los números impares entre 90 y el 130 por orden creciente
    # e) Los múltiplos de 5 entre el 70 y el 25 por orden decreciente (70, 65, ... 30,25).
    
    print("\n[1-50]\n")
    for i in range(1,51):
        print(i)
    print("\n[50-1]\n")
    for i in range(50,0,-1):
        print(i)
    print("\n[%2<20]\n")
    for i in range(2,20,2):
        print(i)
    print("\n[!=%2-90-130]\n")
    for i in range(91,130,2):
            print(i)
    print("\n[%5=70-25]\n")
    for i in range(70,24,-5):
            print(i)
    
def ejer_16(): #Crea un programa que pida al usuario una frase y le diga cuántas vocales tiene esa frase.
    cont=0
    frase=input("Introduce una frase: ")
    for letra in frase:
        if letra in "aeiouAEIOU":
            print(letra)
            l_count+=1
    print(cont)


def ejer_17(): # Vamos a crear una versión del juego Adivina un número en el cual al jugador ha
    # de encontrar un número entre 1 y 100. Dónde.
    # Ø El jugador que inicia el juego tiene que introducir un número entre 1 y 100.
    # Mientras el número no esté en ese rango se siguen pidiendo números. Tras
    # introducir un valor correcto debe borrar la pantalla imprimiendo 50 líneas en blanco.
    # Ø El jugador tienen 5 intentos para encontrar el número. Si el número introducido:
    # · Es menor: mostrará el mensaje es mayor.
    # · Es mayor: mostrará el mensaje es menor.
    # · Si es igual: mostrará el mensaje bien hecho y termina la partida.
    # Ø Si el número de intentos es 0 la partida termina.
    # Ø Siempre al terminar la partida da la opción de salir del juego o comenzar otra partida.
    # Ø Si el número introducido es igual mostrara el mensaje: bien hecho. Has
    # necesitado x intentos. Donde x es el número de intentos realizados.
    
    while True:
        intent=1
        num=int(input('Introduce el número ganador (entre 0-100): '))
        if num>=0 and num<=100:
            print(50*'\n')
            while True:
                num2=int(input('Introduce un número entre 0 y 100: '))
                if intent>5:
                    print('Has utilizado los 5 intentos')
                    break
                elif num2<0 or num2>100:
                    print('El número introducido no está entre 0 y 100')
                elif num==num2:
                    print('Bien hecho, has necesitado',intent,'intentos')
                    break
                elif num>num2:
                    print('El número es mayor que el introducido')
                    intent=intent+1
                elif num<num2:
                    print('El número es menor que el introducido')
                    intent=intent+1
            sel=int(input('Elige 0 para salir o 1 para jugar otra partida: '))
            if sel==0:
                break


def ejer_20():
    while True:
        num1=int(input("Introduce un número entero: "))
        num2=int(input("Introduce otro número entero: "))
        while True:
            calc=int(input("Menu\n    1.Sumar\n    2.Restar\n    3.Multiplicar\n    4.Dividir\n    5.Salir\n Elige una opcion:"))
            if calc == 1:
                print(num1+num2)
            elif calc==2:
                print(num1-num2)
            elif calc==3:
                print(num1*num2)
            elif calc==4:
                print(num1//num2)
            elif calc==5:
                sel=1
                break
            else:
                print("Error")
        if sel==1:
            break
