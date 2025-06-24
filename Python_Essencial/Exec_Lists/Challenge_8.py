pares = []
impares = []


for i in range(0,7):
    valor = int(input('Insira um número:'))

    if valor % 2 == 0:
        pares.append(valor)

    elif valor % 2 == 1:
        impares.append(valor)


num = [pares.copy(),impares.copy()]
num[0].sort()
num[1].sort()

print(f"Os valores pares inseridos são: {num[0]}")
print(f"Os valores impares inseridos são: {num[1]}")