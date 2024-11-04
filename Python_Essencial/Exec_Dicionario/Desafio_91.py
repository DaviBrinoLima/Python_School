import random, time


players = {'Player_1': random.randint(1,6),'Player_2': random.randint(1,6), 'Player_3': random.randint(1,6), 'Player_4': random.randint(1,6) }


print('Valores sorteados:')

for key, values in players.items():
    print(f'O {key} tirou {values}')

    time.sleep(1)


print('Ranking dos Jogadores:')
cont = 1

for key in sorted(players, key= players.get, reverse= True):
    print(f'{cont}° lugar: {key} com {players[key]}')

    cont += 1
    time.sleep(1)