times = ("Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Fluminense", "Athletico-PR", 
    "Atlético-MG", "Fortaleza", "São Paulo", "Cruzeiro", "Internacional", "Red Bull Bragantino", 
    "Cuiabá", "Santos", "Bahia", "Corinthians", "Goiás", "Vasco", "Coritiba", "América-MG")


print(times[0:5])
print(times[16:21])
print(sorted(times))



for pos, i in enumerate(times):
    if i == "Corinthians":
        print(f'Corinthians está na posição {pos+1}')
