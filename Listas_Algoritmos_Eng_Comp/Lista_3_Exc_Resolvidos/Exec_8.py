def exec8():
    soma= 0


    for i in range(1, 501):
        if i%2 == 0:
            soma= soma+i
        
    
    print(f"O somatório dos números pares de 1 a 500 é: {soma}")


if __name__== '__main__':
    exec8()