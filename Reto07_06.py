import random as rd # se importa el paquete random como rd
n=rd.randint(1, 100) #n se inicializa como un numero random entre 1 y 100
bandera:bool=True # se inicializa la bandera
if __name__=="__main__":
    while bandera: #mientras la bandera sea verdadera
        g=int(input("Ingrese el número que adivinas: ")) # g es igual a la entrada por teclado
        if g>n: # si g es mayor a n
            print("El número es menor") # imprimir el número es menor
        elif g<n: # si g es menor a n
            print("El número es mayor") # imprimir el número es mayor
        else: # si no
            break # romper y salir del ciclo
    print(f"Felicidades, adivinaste el número que era {n}") # imprimir "Felicidades, adivinaste el número que era n"