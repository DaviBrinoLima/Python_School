def exec8():
    vetor_1= []
    vetor_2= []
    vetor_3= []


    for i in range (0, 10):
        numero_1= float(input(f"Insira um valor númerico para o index {i} do vetor 1:"))
        vetor_1.append(numero_1)

    print(f"Seu vetor 1 é: {vetor_1}")


    for i in range (0, 10):
        numero_2= float(input(f"Insira um valor númerico para o index {i} do vetor 2:"))
        vetor_2.append(numero_2)

    print(f"Seu vetor 2 é: {vetor_2}")


    for i in range (0,10):
        nummero_3= vetor_1[i] + vetor_2[i]
        vetor_3.append(nummero_3)


    print(vetor_3)


if __name__== '__main__':
    exec8()