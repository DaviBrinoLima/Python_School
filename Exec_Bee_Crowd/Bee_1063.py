def distro_vagoes(train_in : list, train_out : list):
    for _in, _out in zip(train_in, train_out):
        station = []
        result = []
        anchor = _out.pop(0)
        
       
        for vag in _in:
            station.append(vag)
            result.append('I')

            if station[-1] == anchor:
                result.append('R')
                station.pop(-1)
                

        station.reverse()
        anchor = _out.pop(0)
        

        for vag in station:
            if vag == anchor:
                result.append('R')
        
                if _out:
                    anchor = _out.pop(0) 

            else:
                result.append('Impossible')
                break

        
        print(result)



if __name__ == '__main__':
    train_in = []
    train_out = []
    num_vagoes = []


    while True:
        vagoes = int(input('Insira o número de vagões: '))
        num_vagoes.append(vagoes)


        if not vagoes:
            break


        seq_in = (list(input('Insira a sequência de vagões do lado A: ')))
        train_in.append(seq_in)


        seq_out = (list(input('Insira a sequência de vagões do lado B: ')))
        train_out.append(seq_out)


    distro_vagoes(train_in, train_out)
