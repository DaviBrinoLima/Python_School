def exec8():
    a= float(input("Insira um valor para a: "))
    b= float(input("Insira outro valor para b: "))


    troca= a
    a= b
    b= troca


    print(f"Valor invertido de a: {a}")
    print(f"Valor invertido de b: {b}")


if __name__ == '__main__':
    exec8()