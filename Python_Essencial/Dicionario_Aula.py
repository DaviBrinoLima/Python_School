pessoas = {"nome": 'Davi', 'sexo': 'M', 'idade': 22}

print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


###########################################################################################################################################################
for k, v in pessoas.items():
    print(k, v)

for key in pessoas:
    print(key)


###########################################################################################################################################################
pessoas['nome'] = 'Matheus'
pessoas['peso'] = 76

print(pessoas)


###########################################################################################################################################################
brasil = []
estado_1 = {'UF': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado_2 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}

brasil.append(estado_1)
brasil.append(estado_2)

print(brasil[1]['UF'])


estado = {}
for i in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

print(brasil)