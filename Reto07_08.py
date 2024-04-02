def primo (i:int): #se definen los argumentos de la función primo
    j=2 # se inicializa j como 2
    pr:bool=False # se inicializa pr como falos
    while j<i: # mientras j sea mayor a i
        if i%j == 0: # si el residuo de i dividido j es igual a 0
            pr =False # pr es igual a falso
            break # rompe y termina el ciclo
        else: # si no
            pr= True # se actualiza pr como verdadero
        j += 1 # j se actualiza como j+1
    return pr # retorna pr
if __name__ =="__main__": #Función principal
    n=int(input("Ingrese un numero: ")) # n es igual a la entrada de teclado
    i=1 # se inicializa i como 1
    print(f"Los numeros primos desde 1 hasta {n} son: ") # se imprime "Los numeros primos desde 1 hasta n son: "
    while i<=n: # mientras i sea menor o igual a n
        if primo(i): # si lo que la función primo retorna con el argumento i es verdadero
            print(i) # imprime i
        i += 1 # i se actualiza como i+1