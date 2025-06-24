def exec7():
    lado_a= float(input("Insira o lado A do Triângulo: "))
    lado_b= float(input("Insira o lado B do Triângulo: "))
    lado_c= float(input("Insira o lado C do Triângulo: "))


    if (lado_a+lado_b <= lado_c) or (lado_b+lado_c <= lado_a) or (lado_c+lado_a <= lado_b):
        print("Estes valores não são capazes de formar um Triângulo")

    elif lado_a==lado_b==lado_c:
        print("Este valores formam um Triângulo Equilátero")

    elif (lado_a==lado_b) or (lado_b==lado_c) or (lado_c==lado_a):
        print("Estes valores formam um Triângulo Isósceles")

    elif (lado_a!=lado_b and lado_c) and (lado_c!=lado_b):
        print("Estes valores formam um Triângulo Escaleno")
        

if __name__== '__main__':
    exec7()