valor = []


for i in range(0,5):
    num = int(input('Insira um número: '))

    if i == 0 or num > valor[-1]:
        valor.append(num)

    else:
        pos= 0 
        
        while pos < len(valor):
            if num <= valor[pos]:
                valor.insert(pos,num)
                break
            pos += 1


print(valor)