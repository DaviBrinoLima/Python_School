footbal = {'Nome': str(input('Nome do Jogador: ')), 'Partidas': int(input('Número de partidas: '))}


gols = []

for i in range(1, footbal['Partidas'] + 1):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))

footbal['Gols'] = sum(gols)


print('-='*30)

print(f'O jogador {footbal["Nome"]} jogou {footbal["Partidas"]}')


for i in range(0, len(gols)):
    print(f'Na partida {i+1}, fez {gols[i]}')


print(f'Foi um total de {footbal["Gols"]}')
