# 1. Función que continúe pidiendo una cadena mientras solo se introduzcan caracteres de espacio.
def ej1():
    while True:
        cad=input("introduce una cadena: ")
        if cad.strip() == "":
            print("Cadena no válida, vuelve a intentarlo")
        else:
            print("Cadena: ", cad)
            break


# 2. Función a la que se le pasa una cadena y la devuelve al revés.
def ej2base(cad):
    return cad[::-1]

def ej2(cad):
    cad_invert = ej2base(cad)
    print(cad_invert)

#ej2("esta es la cadena")

# 3. Función al que se le pase una cadena, una posición de inicio y una cantidad de caracteres 
# y devuelve el fragmento indicado. Si se le pasan parámetros no válidos devuelve cadena vacía.


# 4. Función que indique si en una cadena todas las palabras comienzan con mayúsculas.



# 5. Escribe una función que compruebe si una palabra es un palíndromo. Un palíndromo es
# una palabra o frase que se lee igual al derecho y al revés.
def ej5base(cad):
    return cad[::-1]

def ej5(cad):
    cad_invert = ej5base(cad)
    if cad==cad_invert:
        print(cad,"es un palíndromo")
    else:
        print(cad,"y",cad_invert,"no se escriben igual")

# ej5("arroz ala zorra")

# 6. Función que dada una cadena devuelve solo las letras mayúsculas que contenga.



# 7. Crea una función que reciba una frase y devuelva el número de palabras de la misma.



# 8. Crea un programa en Python que pida al usuario una cadena y le muestre solo la
# primera letra de cada palabra de la frase en mayúsculas.


# 9. Crea una función que reciba una cadena e invierta el orden de las palabras.



# 10. Crea una función que reciba el nombre y los dos apellidos de un usuario y devuelva su
# identificador, que se formará con las dos primeras letras de su nombre y sus apellidos en mayúsculas.
# Por ejemplo para "Xiana Fernández Rodríguez" su identificador será `XIFERO`.
def ej10(nombre, ape1, ape2):
    id = nombre[:2] + ape1[:2] + ape2[:2]
    print(id.upper())

#ej10("David", "Alvarez", "Pampillon")

# 11. Vamos a jugar a palabras encadenadas. Implementa un programa en Python que a
# partir de una cadena, indique si las palabras que la forman están o no encadenadas.
# Supón que solamente tenemos en cuenta las dos primeras y las dos últimas letras de cada palabra.
def ej11():
    p1=input("Inserta una palabra: ")
    p2=input("Inserta otra palabra: ")
    if p1[-2:] == p2[:2]:
        print(p1, "y", p2, "son palabras encadenadas")
    else:
        print(p1, "y", p2, "NO son palabras encadenadas")
#ej11()


# 12. Crea una matriz de tamaño NxM y que en cada posición almacena un carácter aleatorio
# entre 'A' y 'Z'. Muestra el contenido de la matríz.
import random

def ej12(N, M):
    for i in range(N):
        fila = []  
        for j in range(M):
            letra = chr(random.randint(65, 90))
            fila.append(letra)
        print(' '.join(fila))

#ej12(4,5)

# 13. A partir de dos cadenas, devuelve un conjunto con las letras que estén en ambas.

def ej13():
    cad1=set(input("Inserta la cadena 1:"))
    cad2=set(input("Inserta la cadena 2:"))
    letras_com = cad1.intersection(cad2)
    print("Las letras coincidentes son:", letras_com)

#ej13()

# 14. Escribe un programa que a partir de dos tuplas con el mismo número de elementos,
# una con nombres y otra con edades las convierta en un diccionario donde las claves
# sean los nombres y los valores sean las edades.

def ej14():
    nom = ("David", "Denis", "Alejandro", "Adrian")
    edd = (19, 20, 20, 19)
    dic = dict(zip(nom, edd))
    print(dic)

#ej14()

# 15. Con la intención de organizar mejor la FCT, crea varios conjuntos, uno por cada
# lenguaje de programación que conozcas, y añade a cada uno los alumnos que sepan ese lenguaje.
#
# Acaba de llegar una oferta de empleo que requiere que los candidatos sepan Java, C# y
# Python. ¿Qué alumnos o alumnas podrían optar a ella?

def ej15():
    html = {"David", "Daniel", "Denis"}
    css = {"David", "Alex", "Adrian", "Daniel"}
    python = {"Pepe", "Daniel", "Saul", "David"}
    sql = {"Hugo", "David", "Daniel"}

    selec = html.intersection(css, python, sql)

    print("Los alumnos son:", selec)

# ej15()

# 16. Crea una función de devuelva el número de veces que aparece cada carácter en una
# cadena de texto.
def ej16(cadena):
    cont = {}
    for caracter in cadena:
        if caracter in cont:
            cont[caracter] += 1
        else:
            cont[caracter] = 1
    
    print(cont)

#ej16("hooolllaaalalalalaaoalaaoallao")

# 17. Crea una función de devuelva un diccionario con el número de veces que aparece cada
# palabra en una cadena de texto.

def ej17(cadena):
    palabras = cadena.split()
    cont = {}
    for palabra in palabras:
        if palabra in cont:
            cont[palabra] += 1
        else:
            cont[palabra] = 1
    print(cont)
#ej17("la palabra palabra es la palabra repetida")

# 18. Escribe una función que compruebe si una cadena la cual
# puede contener espacios y signos de puntuación, es palíndromo.
def ej18(cadena):
    cadena = cadena.lower().replace(" ", "")
    cadena = ''.join(caracter for caracter in cadena if caracter.isalnum())
    if cadena == cadena[::-1]:
        print("La cadena", cadena[::-1], "es un palíndromo")
    else:
        print("La cadena NO es un palíndromo(", cadena, "/=", cadena[::-1])

# ej18("arroz, a la zorra")

#-19-#----------------Cifrado César----------------#

def ej19cif(msg, clave):
    result = ""
    for char_inicial in msg:
        if char_inicial.isalpha(): 
            desp = ord('A') if char_inicial.isupper() else ord('a')
            char_final = chr((ord(char_inicial) - desp + clave) % 26 + desp)
            result += char_final
        else:
            result += char_inicial
    print("Msg:", result)

def ej19descif(msg_cif, clave):
    return ej19cif(msg_cif, -clave)

#ej19cif("Este es el mensaje descifrado", 3)
#ej19descif("Hvwh hv ho phqvdmh ghvfliudgr", 3)


# 20. Realiza el juego del ahorcado. Las palabras inicialmente estarán en un vector de 20
# posiciones. Trabaja sólo con mayúsculas. Debe aparecer el dibujo correspondiente a cada fallo.
import random

def ej20graf(intent):
    lose = [
"""






---------
""",
"""
|
|
|
|
|
|
---------
""",
"""
/---\\
|
|
|
|
|
---------
""",
"""
/---\\
|   0
|
|   
|
|
---------
""",
"""
/---\\
|   0
|   |
|   |
|
|
---------
""",
"""
/---\\
|   0
|  /|
|   |
|
|
---------
""",
"""
/---\\
|   0
|  /|\\
|   |
|
|
---------
""",
"""
/---\\
|   0
|  /|\\
|   |
|  /
|
---------
""",
"""
/---\\
|   0
|  /|\\
|   |
|  / \\
|
---------
"""
    ]
    print(lose[intent])

def ej20jugar(selec):
    
    palabra=selec.upper()
    mostrar = ["_"] * len(palabra)
    intent = 0
    intent_max = 8

    letras_intent = set()

    while intent < intent_max:

        print("\n\n\n\n\n\nAdivina la palabra:" + "\n      " + " ".join(mostrar))
        print(f"\nLetras elegidas: {' '.join(sorted(letras_intent))}")
        ej20graf(intent)
        print("      Intentos:",intent,"/ 8")

        letra = input("Dime una letra: ").upper()

        if letra in letras_intent:
            continue
        
        letras_intent.add(letra)
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    mostrar[i] = letra
            if "_" not in mostrar:
                print("\n\n\n\n\n\nHas adivinado la palabra:", palabra)
                break
        else:
            intent += 1
        
        if intent == intent_max:
            print("\n\n\n\n\n\n\n\n\n\nIntentos:",intent,"/ 8")
            print("Has perdido. La palabra era:", palabra)
            ej20graf(intent)

ej20jugar("casa")

