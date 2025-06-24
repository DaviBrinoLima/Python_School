lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#Tuplas são imutáveis
 

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')


print('Comi pra caralho')
# print(sorted(lanche))
# print(lanche)


###########################################################################


a = (2,5,4)
b = (5,8,1,2)

print(b+a)

