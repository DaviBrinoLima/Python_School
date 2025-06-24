def exec9():
    vetor_1= []
    vetor_2= []
    a= float(input("Insira o valor da sua variável A: "))


    for i in range (0, 20):
        numero_1= float(input(f"Insira um valor númerico para o index {i} do vetor 1:"))
        vetor_1.append(numero_1)


    for num in vetor_1:
        numero_2= num*2
        vetor_2.append(numero_2)

        print(f'O seu vetor originado pelo produto do vetor_1 pelo escalar A é: {vetor_2}')


if __name__== '__main__':
    exec9()