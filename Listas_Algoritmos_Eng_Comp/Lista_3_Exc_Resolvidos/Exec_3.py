def exec3():
    num= int(input("Insira um número inteiro positivo: "))
    menor = num


    while num != 0:


        if num > 0:

            if num < menor:
                menor = num


            num= int(input("Insira outro número inteiro positivo: "))


    print(f"O menor número é: {menor}")
        

if __name__== '__main__':
    exec3()
   