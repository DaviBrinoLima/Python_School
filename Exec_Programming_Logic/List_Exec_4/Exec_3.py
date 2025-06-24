def exec3():
    lista_num= []


    for i in range (0,10):
        num= float(input(f"Insira um número: "))
        lista_num.append(num)


    soma=0
    for numero in lista_num:
        soma= soma+numero


    media= round(soma/10, 2)
    
    
    maior_media=0
    for numero in lista_num:
        if numero>media:
            maior_media= maior_media+1


    print(f"A média entre os 10 números digitados é: {media}")
    print(f"A quantidade de números maior que a média é: {maior_media}")


if __name__== '__main__':
    exec3()