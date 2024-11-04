def exec7():
    vetor_1= []


    for i in range (0, 10):
        numero= float(input(f"Insira um valor númerico para o index {i} do vetor:"))
        vetor_1.append(numero)


    vetor_2= []
    for num in vetor_1:
        vetor_2.append(num)


    print(vetor_1)
    print(vetor_2)


if __name__== '__main__':
    exec7()