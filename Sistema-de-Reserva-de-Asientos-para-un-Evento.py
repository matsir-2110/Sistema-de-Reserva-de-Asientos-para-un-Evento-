#Sistema de Reserva de Asientos para un Evento 

#Matriz que representa los asientos del cine
asientos = [['L' for i in range(15)] for j in range(10)]

#Impresión de matriz
for i in range(10):
    print(i+1, "  ", end="")
for i in range(10,15):
    end=print(i+1," ",end="")
print("")
for i in range(10):
    print("  ")
    for j in range(15):
        print(asientos[i][j], "  ", end="")
    print(" ", i+1)

asiento_ocupado = 0
#Usuario ingresa fila
while True:
    while True:
        usu_fila = int(input("\n Ingrese la fila de su asiento (Números indicados a la derecha. MAX = 10):  "))
        usu_fila -= 1
        if usu_fila > 10:
            print("Fila no válida. Intente de nuevo.")

        while True:
            usu_columna = int(input("El numero de su asiento (Números indicados arriba. MAX = 15):  "))
            usu_columna -= 1
            if usu_columna > 15:
                print("Columna no válida. Intente de nuevo.")
            else:
                break

        if asientos[usu_fila][usu_columna] == 'X':
            print("Ese lugar ya esa ocupado, vuelva a ingresar")
        else:
            break

    asientos[usu_fila][usu_columna] = 'X'
    print("¡Perfecto, su asiento ahora reservado!")
    asiento_ocupado += 1
    
    #Seguir ingresando asientos
    opcion = input("¿Desea seguir reservando asientos? (Si/No)  ").lower()
    if opcion == 'si':
        print("Perfecto, los lugares ocupados hasta el momento es: ")
        for i in range(10):
            print(i+1, "  ", end="")
        for i in range(10,15):
            end=print(i+1," ",end="")
        print("")
        for i in range(10):
            print("  ")
            for j in range(15):
                print(asientos[i][j], "  ", end="")
            print(" ", i+1)
    else:
        break

#Impresión final de como quedan los asientos
print("Los asientos ocupados son: ")
for i in range(10):
    print(i+1, "  ", end="")
for i in range(10,15):
    end=print(i+1," ",end="")
print("")
for i in range(10):
    print("  ")
    for j in range(15):
        print(asientos[i][j], "  ", end="")
    print(" ", i+1)

#Última Solicitud al usuario
while True:
    print("¿DESEA VER ALGO MAS? (Ingrese 1,2,3 o 4)")
    print("1. El porcentaje de ocupación actual del auditorio")
    print("2. El número total de asientos libres restantes")
    print("3. La fila con mayor cantidad de asientos libres y cuántos tiene")
    print("4. NO")
    opcion_2 = int(input())
    
    cont = 0
    fila_may = 0
    #Cálculo de porcentaje de ocupación de auditorio [(asientos-ocupados * 100) / total de asientos]
    if opcion_2 == 1:
        print("El porcentaje de asientos ocupados es de: ", (asiento_ocupado * 100)/150)
        opcion_3 = input("Desea volver al menú anterior? (Si/No) ").lower()
        if opcion_3 == 'no':
            break
    #Cálculo de número de asientos restantes
    elif opcion_2 == 2:
        for i in range(10):
            for j in range(15):
                if asientos[i][j] == 'L':
                    cont += 1
        print("El número de asientos libres restantes es: ", cont)
        opcion_3 = input("Desea volver al menú anterior? (Si/No) ").lower()
        if opcion_3 == 'no':
            break
    #Fila con mayor cantidad de asientos libres
    elif opcion_2 == 3:
        for i in range(10):
            cont = 0
            for j in range(15):
                if asientos[i][j] == 'L':
                    cont += 1
            if cont > fila_may:
                fila_may = cont
        print("La fila con mayor cantidad de asientos libres es: ", fila_may)
        print("Y tiene: ", cont, " asientos libres")
        opcion_3 = input("Desea volver al menú anterior? (Si/No) ").lower()
        if opcion_3 == 'no':
            break
    elif opcion_2 == 4:
        print("Bueno Chau")
        break