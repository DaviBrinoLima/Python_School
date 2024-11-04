def exec6():
    salario= float(input("Digite o salário bruto do professor:"))
    
    horas= int(input("Digite a quantidade de aulas dada pelo professor:"))
    # Uma aula = Uma hora


    aula= salario/horas
    print(f"O valor da hora/aula do professor é: {aula}")



    if salario <= 1320:
        desconto= (0.075*salario)
        print(f"O valor do desconto do INSS é: {desconto}")
        salario_com_desconto= salario - desconto
        print(f"O salário líquido do professor é: {salario_com_desconto}")
    
    elif 1320 < salario <= 2580:
        desconto= (0.09*salario)
        print(f"O valor do desconto do INSS é: {desconto}")
        salario_com_desconto= salario - desconto
        print(f"O salário líquido do professor é: {salario_com_desconto}")

    elif 2580 < salario <= 3860:
        desconto= (0.12*salario)
        print(f"O valor do desconto do INSS é: {desconto}")
        salario_com_desconto= salario - desconto
        print(f"O salário líquido do professor é: {salario_com_desconto}")

    elif salario > 3860:
        desconto= (0.14*salario)
        print(f"O valor do desconto do INSS é: {desconto}")
        salario_com_desconto= salario - desconto
        print(f"O salário líquido do professor é: {salario_com_desconto}")


if __name__=='__main__':
    exec6()