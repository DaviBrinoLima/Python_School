def exec12():
    num_1= float(input("Insira o primeiro número: "))
    num_2= float(input("Insira o segundo número: "))


    if num_1%num_2== 0:
        print(f"A divisão de {num_1} por {num_2} É EXATA")

    else:
        print(f"A divisão de {num_1} por {num_2} NÃO É EXATA")


if __name__== '__main__':
    exec12()