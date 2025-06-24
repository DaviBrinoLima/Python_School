def exec6():
    vetor= []

    for i in range (0,15):
        numero= float(input(f"Insira um valor númerico para o index {i} do vetor:"))
        vetor.append(numero)


    maior_elemento= vetor[0]
    menor_elemento= vetor[0]
    posicao_maior= 0
    posicao_menor= 0


    for num in vetor:
        if num>maior_elemento:
            maior_elemento = num
            posicao_maior= vetor.index(num)

        elif num<menor_elemento:
            menor_elemento = num
            posicao_menor= vetor.index(num)

        
    print(f"O maior elemento deste vetor é: {maior_elemento}. Estando ele na posição: {posicao_maior}")
    print(f"O menor elemento deste vetor é: {menor_elemento}. Estando ele na posição: {posicao_menor}")


if __name__== '__main__':
    exec6()