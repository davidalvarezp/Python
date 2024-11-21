tablero=[
    ['o','x','o','o'],
    ['x','o','x','x'],
    ['o','o','o','x'],
    ['o','o','o','o']    
]

j1='x'
j2='o'
tam=len(tablero)

def filas(tablero, jugador):
    for filas in tablero:
        aux="".join(filas)
        if aux==jugador*tam:
            return True
    return False

def colum(tablero, jugador):
    for i in range(tam):
        aux=""
        for j in range(tam):
            aux+=tablero[j][i]
        if aux==jugador*tam:
            return True
    return False

def diag1(tablero, jugador):
    aux=""
    for i in range(tam):
        aux+=tablero[i][i]
    es_igual= aux==jugador*tam
    print("Es igual?",es_igual)
    return es_igual

def diag2(tablero, jugador):
    # 2 0
    # 1 1
    # 0 2
    aux=""
    for i in range(len(tablero)-1,-1,-1):
        aux+=tablero[i][len(tablero)-1-i]
    return aux==jugador*tam;    


def hay_3_en_rayaa(tablero, jugador):
    if filas(tablero, jugador): 
        return True;
    if colum(tablero, jugador): 
        return True;
    if diag1(tablero, jugador): 
        return True;
    if diag2(tablero, jugador): 
        return True;
    return False;

def hay_3_en_rayab(tablero, jugador):
    return filas(tablero, jugador) or colum(tablero, jugador) or diag1(tablero, jugador) or diag2(tablero=jugador)




def ver(tablero):
    for filas in tablero:
        print(filas)

ver(tablero)
print(diag1(tablero, j2))
# print(diag1(tablero, j2))
