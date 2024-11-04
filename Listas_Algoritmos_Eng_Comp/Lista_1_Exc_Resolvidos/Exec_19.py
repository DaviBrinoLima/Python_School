def exec19():
    import math


    tanques= int(input("Insira a quantidade de tanques a serem pintados: "))
    altura= int(input("Insira a altura dos tanques em metros: "))
    raio= int(input("Insira o raio dos tanques: "))

    
    area= round((2*3.14) * (raio) * (altura+raio), 2)
    print(f"A quantidade de metros quadrados a serem pintados: {area} m2")


    #Cada lata de tinta custa 50 reais
    #Cada lata de tinta contém 5 litros de tinta
    #Cada litro de tinta pinta 3 mˆ2


    latas_necessarias= math.ceil(area/15)
    print(f"A quantidade de latas necessárias para pintar os tanques é: {latas_necessarias} latas de tinta")


    custo_latas= latas_necessarias*50
    print(f"O custo para pintar os tanques será: {custo_latas} reais")


if __name__== '__main__':
    exec19()
