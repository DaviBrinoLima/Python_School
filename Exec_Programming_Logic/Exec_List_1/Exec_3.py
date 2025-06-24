def exec3():
    
    raio= float(input("Digite o raio da lata: "))
    altura= float(input("Digite a altura da lata: "))
    
    
    area= 3.14159*(raio**2)
    volume= area*altura


    print(f"O volume da lata é: {volume} ")


if __name__=='__main__':
    exec3()