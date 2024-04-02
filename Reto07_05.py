if __name__=="__main__":
    n=int(input("Ingrese un numero: ")) # n inicializa como la entrada de teclado
    i = n-1 # i inicializa como n-1
    a=n #a inicializa como n
    while i>=1: # mientras i sea mayor o igual a 1
        a *= (i) # a se actualiza como a*i
        i -= 1 # i se actualiza como i-1
    print(f"El factorial de {n} es igual a {a}") # imprime "El factorial de n es igual a a"