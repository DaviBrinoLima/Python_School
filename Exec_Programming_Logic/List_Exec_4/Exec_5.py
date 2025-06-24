def exec5():
    vetor= []


    for i in range (0,10):
        num= float(input("Insira um valor para seu vetor: "))
        vetor.append(num)


    negativos= 0 
    soma_positivos= 0

    for valor in vetor:
        if valor<0:
            negativos= negativos+1

        elif valor>0:
            soma_positivos= round(soma_positivos+valor, 2)


    print(f"A quantidade de números negativos neste vetor é: {negativos}")
    print(f"A soma dos números positivos deste vetor é: {soma_positivos}")


if __name__== '__main__':
    exec5()