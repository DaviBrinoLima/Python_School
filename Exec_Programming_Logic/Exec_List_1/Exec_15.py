def exec15():
    a= int(input("Insira o primeiro número: "))
    b= int(input("Insira o segundo número: "))  
    c= int(input("Insira o terceiro número: "))


    operacao= ((a**2) + (b**2) + (c**2) + (2*((a*b) + (a*c) + (b*c))))
    print(f"O resultado do quadrado da soma dos 3 termos é: {operacao}")


if __name__== '__main__':
    exec15()