def exec11():
    jogadores= []
    altura= []


    for i in range (12):
        nome= input("Insira o nome do jogador: ")
        altura_jogador= float(input("Insira a altura do Jogador em metros: "))


        jogadores.append(nome)
        altura.append(altura_jogador)


    maior_altura= 0


    for num in altura:
        if num>maior_altura:
            maior_altura= num

    
    nome_mais_alto= altura.index(maior_altura)
    print(jogadores[nome_mais_alto], maior_altura)


exec11()