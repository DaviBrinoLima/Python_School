import random

def exec4():
    soma_2= 0
    soma_3= 0
    soma_4= 0
    soma_5= 0
    soma_6= 0
    soma_7= 0
    soma_8= 0
    soma_9= 0
    soma_10= 0
    soma_11= 0
    soma_12= 0


    for i in range (0,36000):
        dado_1= random.randint(1,6)
        dado_2= random.randint(1,6)

        soma_dados= dado_1+dado_2


        if soma_dados==2:
            soma_2= soma_2+1

        elif soma_dados==3:
            soma_3= soma_3+1

        elif soma_dados==4:
            soma_4= soma_4+1

        elif soma_dados==5:
            soma_5= soma_5+1

        elif soma_dados==6:
            soma_6= soma_6+1

        elif soma_dados==7:
            soma_7= soma_7+1

        elif soma_dados==8:
            soma_8= soma_8+1

        elif soma_dados==9:
            soma_9= soma_9+1

        elif soma_dados==10:
            soma_10= soma_10+1

        elif soma_dados==11:
            soma_11= soma_11+1

        else:
            soma_12= soma_12+1


    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_2}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_3}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_4}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_5}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_6}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_7}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_8}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_9}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_10}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_11}")
    print(f"A quantidade de vezes onde a soma dos dados foi 2 é: {soma_12}")
   

def func():
    somas = [0 for i in range(11)]
    for i in range(36000):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        somas[d1+d2-2] += 1
        

    print(somas)
if __name__== '__main__':
    lista = ["Matheus", "Davi", "Andressa"]
    i = 0
    i+=1
    lista[i] = "Davi1"
    print(lista[i])