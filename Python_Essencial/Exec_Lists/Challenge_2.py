valor = []


while True:
    num = int(input('Insira um número: '))

    if num not in valor:
        valor.append(num)
    
    elif num in valor:
        print('Este número já existe na lista')
        break


valor.sort()
print(valor)

