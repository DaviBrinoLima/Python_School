def exec1():
    soma=0
    

    for i in range(1,100):


        if i%2==1:
            soma= soma+i


    print(f"A soma dos números ímpares de 1 a 99 é: {soma}")
        

if __name__ == '__main__':
    exec1()