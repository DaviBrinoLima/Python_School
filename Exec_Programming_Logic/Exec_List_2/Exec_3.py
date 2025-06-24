def exec3():
    nota_1= float(input("Insira a primeira nota: "))
    nota_2= float(input("Insira a segunda nota: "))
    nota_3= float(input("Insira a terceira nota: "))
    nota_4= float(input("Insira a quarta nota: "))


    media= round((nota_1+nota_2+nota_3+nota_4)/4, 1)


    if media >= 7:
        print(f"O aluno foi APROVADO, sua media final é: {media}")

    else:
        exame= float(input("Insira a nota do exame: "))
        nova_media= round((media*0.6)+(exame*0.4), 1)


        if nova_media >= 5:
            print(f"O aluno foi APROVADO EM EXAME, sua media final é: {nova_media}")

        else: 
            print(f"O aluno foi REPROVADO, sua media final é: {nova_media}")
        

if __name__== '__main__':
    exec3()