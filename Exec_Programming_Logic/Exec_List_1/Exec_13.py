def exec13():
    a= int(input("Insira o primeiro número inteiro: "))
    b= int(input("Insira o segundo número inteiro: "))
    c= int(input("Insira o terceiro número inteiro: "))


    operacao= ((a**2) + (b**2) + (c**2))
    print(f"O valor da soma dos quadrados dos 3 número é: {operacao}")


if __name__== '__main__':
    exec13()