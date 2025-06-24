aluno = {}

aluno['Nome'] = str(input('Insira o nome do aluno: '))
aluno['Média'] = float(input('Insira a média: '))


if aluno['Média'] > 7:
    aluno['Situação'] = 'Aprovado'

else: 
    aluno['Situação'] = 'Reprovado'


for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')