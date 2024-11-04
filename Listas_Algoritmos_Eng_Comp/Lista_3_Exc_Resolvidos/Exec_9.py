def exec9():
    soma_par= 0
    soma_impar= 0


    for i in range(300, 501):
        if i%2 == 0:
            soma_par= soma_par+i


    for i in range(50, 101):
        if i%2 == 1:
            soma_impar= soma_impar+i
        
    
    soma_final= soma_par - soma_impar
    print(f"A diferença entre essas duas somas é: {soma_final}")
    

if __name__== '__main__':
    exec9()