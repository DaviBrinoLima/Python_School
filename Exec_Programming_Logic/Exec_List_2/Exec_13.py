def exec13():
    produto= float(input("Insira o valor do produto:"))


    if produto<20:
        lucro= produto*0.45
        vendas= round(produto+lucro, 2)
        print(f"O valor de venda do produto é: {vendas}")

    else:
        lucro= produto*0.30
        vendas= round(produto+lucro, 2)
        print(f"O valor de venda do produto é: {vendas}")


if __name__== '__main__':
    exec13()
