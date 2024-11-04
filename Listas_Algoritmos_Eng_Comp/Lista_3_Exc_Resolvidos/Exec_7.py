def exec7():
    num= int(input("Digite o número a ter a tabuada consultada:"))
    n_vezes= int(input("Digite até qual valor a tabuada deve ser executada: "))


    tabuada= 0


    for i in range(0, n_vezes+1):
        tabuada= num*i
        print(tabuada)


if __name__== '__main__':
    exec7()
