i=1 # inicializa i como 1
impar:bool=True #inicializa la variable impar como verdadera
if __name__=="__main__":
    while i<=100: # mientras i sea menor o igual a 100
        if impar: # condicional si impar (si impar es verdadera)
            print(i) # imprimir i 
            i += 2 # actualizar i como i+2
            if i>=100: # si i es mayor o igual a 100
                impar = False # actualiza impar como falso
                i = 2 # actualiza i como 2
        else: # si la condición impar como verdadero no se cumple
            print(i) # imprimir i
            i+=2 # actualizar i como i+2