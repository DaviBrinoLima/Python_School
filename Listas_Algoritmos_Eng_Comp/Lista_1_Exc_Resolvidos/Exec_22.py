def exec22():
    horas= int(input("Insira as horas: "))
    minutos= int(input("Insira os minutos: "))
    segundos= int(input("Insira os segundos: "))


    segundos_horas= horas*3600
    segundos_minuto= minutos*60


    segundos_total= segundos_horas+segundos_minuto+segundos
    print(f"O total de segundos nessas horas, minutos e segundos é: {segundos_total} segundos")


if __name__=='__main__':
    exec22()
