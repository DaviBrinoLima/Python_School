def exec15():
    massa= float(input("Informe o peso em Kg: "))
    altura= float(input("Informe a altura em metros: "))


    imc= massa/(altura**2)


    if imc<20:
        print("Sua faixa de risco é: ABAIXO DO PESO")


    elif imc>=20 and imc<25:
        print("Sua faixa de risco é: NORMAL")


    elif imc>=25 and imc<30:
        print("Sua faixa de risco é: EXCESSO DE PESO")


    elif imc>=30 and imc<35:
        print("Sua faixa de risco é: OBESIDADE")


    else:
        print("Sua faixa de risco é: OBESIDADE MÓRBIDA")


if __name__== '__main__':
    exec15()
