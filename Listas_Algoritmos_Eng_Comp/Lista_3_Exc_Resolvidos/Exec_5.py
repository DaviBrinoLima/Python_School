def exec5():
    num= int(input("Insira um número positivo: "))
    
    
    lista= []
    lista.append(num)
    
    
    contador= 0


    while num!=0:
        num= int(input("Insira outro número inteiro: "))
        lista.append(num)


        contador= contador+1


    print(f"Sua lista possue: {contador} elementos")
    n_posicoes= int(input("Insira quantos elementos da lista serão operadas: "))
    nova_lista = []


    while n_posicoes>contador:
        print(f"A lista possue menos elementos que o números a serem operados")
        n_posicoes= int(input("Insira uma nova quantia de elementos a serem operadas: "))    
    

    for i in range(n_posicoes):
        nova_lista.append(lista[i])


    soma= 0
    quadrado= 0


    for i in nova_lista:
        soma= soma+i
        quadrado= quadrado + (i**2)

    
    media= round(soma/n_posicoes, 2)


    print(f"O somatório dos elementos operados é: {soma}")
    print(f"A soma dos quadrados dos elementos operados é: {quadrado}")
    print(f"A média dos elementos operados é: {media}")


if __name__== '__main__':
    exec5()