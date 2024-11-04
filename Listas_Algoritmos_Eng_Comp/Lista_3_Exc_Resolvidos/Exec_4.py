def exec4():
    num= int(input("Insira um número inteiro positivo: "))
    lista= []


    lista.append(num)


    while num != 0:
        num= int(input("Insira outro número inteiro: "))
        lista.append(num)


    impar= 0

    for i in lista:
        if i%2 == 1:
            impar=  impar+1

    
    print(f"A quantidade de número ímpares digitados pelo usuário é: {impar}")


if __name__== '__main__':
    exec4()
