def exec2():
    num_times= int(input("Insira a quantidade de times que participaram do campeonato: "))
    
    while num_times>50:
        num_times= int(input("A quantidade de times é maior que o limite permitido (50), insira novamente o número de times que participaram: "))


    lista_pontuacao= []


    for i in range (0, num_times):
        pontuacao= int(input(f"Insira a pontuação do time {i}: "))
        lista_pontuacao.append(pontuacao)


    pontuacao_maxima= 0
    campeoes= 0
    pontuacao_campeoes= 0
    
    for i in lista_pontuacao:
        if i>pontuacao_maxima:
            campeoes= 1
            pontuacao_maxima= i

        elif i==pontuacao_maxima:
            campeoes= campeoes+1
            pontuacao_campeoes= pontuacao_maxima+i


    print(f"A quantidade de times que ganharam o campeonate é: {campeoes} ")
    print(f"A pontuação máxima obtida no campeonato foi: {pontuacao_maxima}")
    print(f"A soma das pontuações dos campeões é: {pontuacao_campeoes}")



if __name__== '__main__':
    exec2()