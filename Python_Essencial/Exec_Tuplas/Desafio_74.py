import random
random.seed(34)


aux = []

for i in range(0,5):
    aux.append(random.randint(0,99))

num = tuple(aux)
print(num)


maior = 0
menor = 99

for i in num:
    if i > maior:
        maior = i

    elif i < menor:
        menor = i


print(f'O Maior número da tupla é: {maior}')
print(f'O Menor número da tupla: {menor}')
