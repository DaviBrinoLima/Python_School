def exec7():
    tempo= float(input("Digite o tempo gasto na viagem em horas: "))
    # 1= Uma hora e 0.1= 6 minutos

    velocidade= float(input("Digite a velocidade média do carro durante a viagem km/h:"))


    distancia= tempo*velocidade
    
    consumo= distancia/12
    # O carro faz 12 km com 1 litro de combustível

    print(f"O tempo gasto na viagem foi: {tempo} horas, onde 0.1 = 6 Minutos")

    print(f"A velocidade média durante a viagem foi: {velocidade} km/h")

    print(f"A distância percorrida na viagem foi: {distancia} km")

    print(f"O consumo do Veículo neste viagem foi: {consumo} litros de combustível")


if __name__ == '__main__':
    exec7()
    
