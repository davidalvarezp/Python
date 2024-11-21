hora = input("Insertar hora:")
min = input("Insertar minuto:")
dura = input("Insertar la duración (mins):")

dura_horas = int(dura)//60
dura_mins = int(dura)%60

print("El evento acaba a las ",int(hora)+dura_horas,":",int(min)+dura_mins)