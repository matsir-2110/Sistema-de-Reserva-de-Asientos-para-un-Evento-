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

#Usuario ingresa fila
while True:
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