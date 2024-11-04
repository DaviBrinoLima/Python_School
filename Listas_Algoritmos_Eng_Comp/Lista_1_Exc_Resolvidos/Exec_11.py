def exec11():
    dolar= float(input("Insira o valor em dolár a ser convertido: "))
    cotacao= float(input("Insira a cotação atual do dolár: "))


    real= dolar*cotacao
    print(f"A conversão em real deste valor é: {real} reais")


if __name__== '__main__':
    exec11()