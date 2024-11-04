num = []
maior = 0
menor = 99


for i in range(0,5):
    num.append(int(input('Insira um número: ')))


for i in num:
    if i > maior:
        maior = i

    elif i < menor:
        menor = i


print(f'O menor valor é {menor} e sua posição é {num.index(menor)}')
print(f'O maior valor é {maior} e sua posição é {num.index(maior)}')