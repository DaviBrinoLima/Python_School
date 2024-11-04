inserir = []
pessoas = []

maior = 0
menor = 300


while True:
    inserir.append(str(input('Insira o nome: ')))
    inserir.append(float(input('Insira o peso: ')))

    pessoas.append(inserir.copy())


    if maior < inserir[1]:
        maior = inserir[1]
    
    if menor > inserir[1]:
        menor = inserir[1]
    

    pergunta = input('Deseja Continuar? (Responda com y ou n): ')


    if pergunta == 'y':
       inserir.clear()

    elif pergunta == 'n':
        break


pesadas = []
leves = []


for i in pessoas:
    if i[1] == maior:
        pesadas.append(i[0])

    elif i[1] == menor:
        leves.append(i[0])


print(f'O total de pessoas cadastradas é: {len(pessoas)}')
print(f'O maior peso é {maior} e ele pertence a: {pesadas}')
print(f'O menor peso é {menor} e ele pertence a: {leves}')

    
