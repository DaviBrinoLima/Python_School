def exec1():
    
    n1 = input("Digite um número inteiro: ")
    while not n1.isnumeric():
        n1 = input("Isto não é um inteiro! Digite outro número: ")
    

    n2 = input("Digite um segundo número inteiro: ")
    while n2[0]=="0" or "." in n2 or "," in n2:
        if "." in n2 or "," in n2 : 
            n2= input("Isto não é um inteiro! Escreva outro número: ")
        elif n2[0] == "0" :
            n2= input("Divisão por zero! Escreva outro número: ")
    n1=int(n1)
    n2=int(n2)


    soma= n1+n2
    produto = n1*n2

    if n2 == 0:
        print(f"Divisão: Divisão por zero")
    else :
        div= n1/n2
        print(f"Soma: {soma}, Produto: {produto}, Divisão: {div}")


if __name__=='__main__':
    exec1()