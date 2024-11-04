def exec9():
    num= int(input("Insira um número inteiro de 0 até 10: "))


    if num>= 0 and num<=10:
        if num==0:
            print("O seu número escrito por extenso é zero")


        elif num==1:
            print("O seu número escrito por extenso é um")


        elif num==2:
            print("O seu número escrito por extenso é dois")


        elif num==3:
            print("O seu número escrito por extenso é três")


        elif num==4:
            print("O seu número escrito por extenso é quatro")


        elif num==5:
            print("O seu número escrito por extenso é cinco")


        elif num==6:
            print("O seu número escrito por extenso é seis")


        elif num==7:
            print("O seu número escrito por extenso é sete")


        elif num==8:
            print("O seu número escrito por extenso é oito")


        elif num==9:
            print("O seu número escrito por extenso é nove")


        else:
            print("O seu número escrito por extenso é dez")


    else:
        print("O número informado não está dentro da faixa permitida")

    
if __name__== '__main__':
    exec9()