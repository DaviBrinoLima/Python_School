def exec10():
    lista_par= []
    lista_impar= []


    for i in range (30):
        conjunto= int(input("Insira um valor númerico: "))


        if len(lista_par) < 15:
            if conjunto%2==0: 
                lista_par.append(conjunto)

        
        if len(lista_par)== 15:
            print("O Vetor par já possui 15 elementos")


        if len(lista_impar) < 15:
            if conjunto%2==1: 
                lista_impar.append(conjunto)


        if len(lista_impar)== 15:
            print("O Vetor impar já possui 15 elementos")


    print(lista_par)
    print(lista_impar)


if __name__== '__main__':
    exec10()


        