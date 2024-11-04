num = []


for i in range(0,10):
    num.append(int(input('Insira um número: ')))


print(len(num))


num.sort(reverse= True)
print(num)


if 5 in num:
    print('O número 5 está contido na lista')