def exec12():
    vetor_4= []

    for i in range (5):
        posicao_1= float(input(f"Insira um número a posição {i} do seu vetor 1:"))
        posicao_2= float(input(f"Insira um número a posição {i} do seu vetor 2:"))
        posicao_3= float(input(f"Insira um número a posição {i} do seu vetor 3:"))


        posicao_4= round((posicao_1*posicao_3)/posicao_2, 2)
        vetor_4.append(posicao_4)


    print(vetor_4)


exec12()