if __name__=="__main__":
    n=int(input("Ingrese un numero: ")) # lee la entrada de teclado como n
    print(f"Números pares menores a {n}") # imprime un encabezado que dice "Numeros pares menores a " n
    i=n # inicializa i como n
    while i>=1: # mientras i sea mayor o igual a 1
        if n%2!=0: # si n no es divisible por 0 (n es impar)
            i-= 1 # se actualiza i como i-1
        print(i) # se imprime i
        i-=2 # actualiza i como i-2