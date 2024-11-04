list_aux = []

for i in range(0,4):
    list_aux.append(int(input("Insira um número: ")))

nums = tuple(list_aux)


print(f'O número 9 apareceu {nums.count(9)} vezes')
print(f'O número aparece pela primeira vez na posição {nums.index(3)}')


pares = 0

for i in  nums:
    if i%2 == 0:
        pares += 1


print(f'Os números pares digitados foram: {pares}')