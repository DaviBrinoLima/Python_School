def exec2():
    num_1= int(input("Insira o primeiro número inteiro: "))
    num_2= int(input("Insira o segundo número inteiro: "))

    
    if num_1>num_2:
        diferenca= num_1-num_2
        print(f"O resultado da diferença do maior pelo menor é: {diferenca}")

    else:
        diferenca= num_2-num_1
        print(f"O resultado da diferença do maior pelo menor é: {diferenca}")


if __name__=='__main__':
    exec2()
