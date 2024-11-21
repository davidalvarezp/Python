
# #------Ejercicios------#

def ejer_1(): #Utiliza la función print para imprimir la cadena "Hola" por la pantalla.
    
    print("Hola")

#def ejer_2(): #Elimina las comillas de la instrucción anterior y ejecútala. ¿Qué de error se produce? ¿Qué significa ese error?.

    #print(Hola)     #NameError: name 'Hola' is not defined

def ejer_3(): #Utiliza la función print para imprimir la cadena "Hola mundo" por la pantalla.

    print("Hola mundo")

def ejer_4(): #Cambia las comillas dobles por comillas simples. ¿Qué sucede?.

    print('Hola mundo')     #No sucede nada

#def ejer_5(): #Elimina las comillas de la instrucción anterior y ejecútala. ¿Qué de error se produce? ¿Qué significa ese error?.

    #print(Hola mundo)       #SyntaxError: invalid syntax. Perhaps you forgot a comma?

#def ejer_6(): #Ejecuta la siguiente instrucción: print “hola mundo” ¿Qué sucede y por qué?

    #print "Hola mundo"      #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#def ejer_7(): #En una misma línea ejecuta dos instrucciones print con el texto que desees.

    #print("Hola") print("mundo")    #SyntaxError: invalid syntax

#def ejer_8(): #Ejecuta estas instrucciones print:
# #   print("2+3")        Muestra 2+3
# #   print(2+3)          Muestra 5
# #   print("2"+"3")      Muestra 5
# #   Print("2+3")        Error: print no Print
# #   print(2"+"3)        Error: las comillas mal utilizadas
# #¿Qué muestran?¿Por qué?

def ejer_(): #Muestra la ayuda del comando print

    help(print)

#-------------------------------------------------------------------------#

def ejer_10(): #Muestra en un único print varias cadenas diferentes separadas por un tabulador.

     print('''Cadenas    separadas
              por     un      tabulador''')


#-------------------------------------------------------------------------#

def ejer_11(): #Muestra una única cadena que en su interior ha de tener una comilla simple,
    # una comilla doble y una barra invertida. Define la cadena tanto con comillas simples como con comillas dobles.

    print("6+"'3' " "" es igual a nueve")
    print('Eduardo dijo:"\\\' " ')

#-------------------------------------------------------------------------#

def ejer_12(): #Realiza un programa que pida dos números al usuario y los sume

    n1 = input("Primer numero: ")

    n2 = input("Segundo numero: ")

    suma = int(n1) + int(n2)

    print("La suma de esos números es: ", suma)

#-------------------------------------------------------------------------#

def ejer_13(): #Crea un programa que pida al usuario una base y un exponente y muestre el valor de elevar la base al exponente.

    n1 = input("Base: ")

    n2 = input("Exponente: ")

    valor = int(n1) ** int(n2)

    print("El resultado de ", int(n1), " elevado a ", int (n2), " es: ", valor)

#-------------------------------------------------------------------------#

def ejer_14(): #Crea un programa que dada una cantidad en euros, devuelve su valor en dólares.

    n1 = input("Inserte cantidad en €: ")

    valor = int(n1) * 1.11

    print(int(n1),"€ equivalen a", valor,"$")

#-------------------------------------------------------------------------#

def ejer_15(): #Crea un programa que dada una cantidad en dólares, devuelve su valor en euros.

    n1 = input("Inserte cantidad en $: ")

    valor = int(n1) * 0.89

    print(int(n1),"$ equivalen a", valor,"€")

#-------------------------------------------------------------------------#

def ejer_16(): #Crea un programa que a partir de la hora de comienzo de un evento y su
# duración (3 valores: hora, minutos, duración en minutos) calcula la hora de
# finalización del evento. No te preocupes de los errores que pueda introducir el
# usuario (hora inválida). PISTA: Emplea el operador módulo (`%`)

    hora = int(input("Insertar hora:"))
    min = int(input("Insertar minuto:"))
    dura = int(input("Insertar la duración (mins):"))

    dura_horas = dura//60
    dura_mins = dura%60

    print("El evento acaba a las ",hora+dura_horas,":",min+dura_mins)

#-------------------------------------------------------------------------#

def ejer_17(): #Crea un programa que calcule y muestre el IMC (índice de masa corporal) de un usuario. Para ello debe:
# Ø Pedir el nombre de un usuario
# Ø Pedir su peso
# Ø Pedir su altura (en metros)
# Calcular el IMC según la siguiente fórmula: (peso / altura2)

    print("")

#-------------------------------------------------------------------------#

def ejer_18(): #A partir de tres datos a, b, c calcula el resultado de la siguiente operación:
# (a+b+c)3

    print("")


#-------------------------------------------------------------------------#

def ejer_6_1(): #Implementa un programa en Python que pida por teclado un número entero y que indique
    #si es par (si es impar, no muestra nada).
   
    print("")

def ejer_6_2(): #2. Modifica el programa para que indique si es par o impar.
   
    print("")

def ejer_6_3(): #Implementa un programa en Python que pida dos números por teclado y que muestre por
    #pantalla al menor de los dos o si son iguales.
    print("")


def ejer_6_4(): #Implementa un programa en Python que pida un número por teclado y que muestre por
    #pantalla un mensaje indicando si es o no negativo. El 0 no es negativo.
  
    print("")

def ejer_6_5(): #Implementa un programa en Python que pida tres números por teclado y muestre por
    #pantalla el mayor de los tres.
    
    print("")

def ejer_6_6(): #Implementa un programa en Python para mostrar por pantalla la calificación de una nota
    #a partir de la puntuación introducida por teclado:
        # [0,5) Suspenso
        # [5,6) Aprobado
        # [6,7) Bien
        # [7,9) Notable
        # [9,10] Sobresaliente
    
    print("")
