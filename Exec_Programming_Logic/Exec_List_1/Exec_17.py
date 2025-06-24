def exec17():
    salario= float(input("Digite o  salário do trabalhador: "))
    ajuste= float(input("Digite em quantos porcento o salário será ajustado: "))


    porcentagem_real= ajuste/100
    valor_ajuste= salario*porcentagem_real


    salario_ajustado= salario + valor_ajuste
    print(f"O valor do novo salário é: {salario_ajustado}")


if __name__== '__main__':
    exec17()