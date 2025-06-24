def exec14():
    salario= float(input("Informe o salário: "))


    if salario<=400:
        print("O salário será aumentado em 15%")


        aumento= salario*0.15
        salario_novo= round(salario+aumento, 2)

        print(f"O salário aumentado é: {salario_novo} reais")

    
    elif salario>=400.01 and salario<=700:
        print("O salário será aumentado em 12%")


        aumento= salario*0.12
        salario_novo= round(salario+aumento, 2)

        print(f"O salário aumentado é: {salario_novo} reais")


    elif salario>=700.01 and salario<=1000:
        print("O salário será aumentado em 10%")


        aumento= salario*0.10
        salario_novo= round(salario+aumento, 2)

        print(f"O salário aumentado é: {salario_novo} reais")


    elif salario>=1000.01 and salario<=1800:
        print("O salário será aumentado em 7%")


        aumento= salario*0.07
        salario_novo= round(salario+aumento, 2)

        print(f"O salário aumentado é: {salario_novo} reais")


    elif salario>=1800.01 and salario<=2500:
        print("O salário será aumentado em 5%")


        aumento= salario*0.05
        salario_novo= round(salario+aumento, 2)

        print(f"O salário aumentado é: {salario_novo} reais")


    else:
        print("Este salário não sofrerá aumento")


if __name__== '__main__':
    exec14()