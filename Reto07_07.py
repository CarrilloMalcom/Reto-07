if __name__=="__main__":
    n=int(input("Ingrese un numero: ")) # n se inicializa igual a la entrada por teclado
    i=1 # i se inicializa como 1
    print(f"Los divisores de {n} son: ") # imprimir "Los divisores de n son: "
    while i<=n: # mientras i sean menor o igual a 1
        if n%i==0: # si el residuo de n dividido i es igual a 0
            print(i) # imprimir i
        i += 1 # i se actualiza como i+1