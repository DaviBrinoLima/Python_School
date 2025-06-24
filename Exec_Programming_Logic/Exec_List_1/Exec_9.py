def exec9():
    comprimento= float(input("Insira o comprimento da caixa: "))
    largura= float(input("Insira a largura da caixa: "))
    altura= float(input("Insira a altura do caixa: "))


    area= comprimento*largura
    print(f"A área da caixa é: {area} metros quadrados")

    volume= area*altura
    print(f"O volume da caixa é: {volume} metros cúbicos ")


if __name__== '__main__':
    exec9()


    