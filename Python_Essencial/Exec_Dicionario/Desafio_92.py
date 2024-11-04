worker = {'Nome': str(input('Nome: ')), 'Idade': int(input('Ano de Nascimento: ')), 'CTPS': int(input('Carteira de Trabalho (0 para não tem): '))}

if worker['CTPS'] != 0:
    worker['Contract'] = int(input('Ano de contratação: '))
    worker['Salario'] = float(input('Salário: '))


aposent = 65 + worker['Idade']
worker['Aposent'] = aposent


print('-='*30)

for key, value in worker.items():
    print(f"{key} tem o valor {value}")