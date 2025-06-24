def exec14():
    balas= int(input("Digite a quantidade de balas que serão distribuídas:"))
    pessoas= int(input("Digite para quantas pessoas estas balas serão distribuídas: "))


    balas_pessoas= balas//pessoas
    resto= balas - balas_pessoas*pessoas


    print(f"A quantidade de balas que cada pessoa deve receber é: {balas_pessoas}")
    print(f"A quantidade de balas restante é: {resto}")


if __name__== '__main__':
    exec14()
