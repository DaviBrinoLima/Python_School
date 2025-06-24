num = [2,5,9,1]
print(num)


num.append(7)
num.insert(2,8)
num.pop(3)

print(num)


##########################################################################
a = [2,3,4,7]
b=a


b[2] = 8
print(f'{a} and {b}')


###########################################################################
a = [2,3,4,7]
b= a[:]


b[2] = 8
print(f'{a} and {b}')


###########################################################################
dados = []
dados.append('Gustavo')
dados.append(20)


pessoa = []
pessoa.append(dados.copy())


dados[0] = 'Maria'
dados[1] = 22
pessoa.append(dados.copy())


print(pessoa)
print(pessoa[0][0])


for p in pessoa:
    print(f"{p[0]} tem {p[1]} anos de idade")