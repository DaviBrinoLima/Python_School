def exec12():
    real= float(input("Insira o valor em real a ser convertido: "))
    cotacao= float(input("Insira a cotação atual do dolár: "))


    dolar= round(real/cotacao, 2)
    print(f"A conversão em dolár deste valor é: {dolar} dolares")


if __name__== '__main__':
    exec12()