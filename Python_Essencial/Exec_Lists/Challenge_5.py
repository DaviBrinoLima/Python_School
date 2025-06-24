lista = []
pares = []
impar = []


for i in range(0,10):
    num = int(input('Insira um número: '))
    lista.append(num)

    if num % 2 == 0:
        pares.append(num)

    elif num % 2 == 1:
        impar.append(num)


print(lista)
print(pares)
print(impar)

    