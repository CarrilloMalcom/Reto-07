A:int=25000000 # inicializa la variable A como un entero de 25000000
B:int=18900000 # inicializa la variable B como un entero de 18900000
i:int=0 # inicializa i como 0
if __name__=="__main__":
    while A>=B: # mientras A sea mayor o igual a B
        i += 1 # i se actualza  como i+1
        A += (A*0.02) # A se actualiza como A+(A*2%)
        B += (B*0.03) # B se actualiza como B+(B*3%)
    print(f"El país B superará al país A en población en {i} años, es decir en {2022+i}") # imprimir "El país B superará al país A en población en i años, es decir en 2022+i"
