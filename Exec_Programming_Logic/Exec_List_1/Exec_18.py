def exec18():
    votos_a= int(input("Insira a quantidade de votos do candidato A: "))
    votos_b= int(input("Insira a quantidade de votos do candidato B: "))
    votos_c= int(input("Insira a quantidade de votos do candidato C: "))


    votos_nulos= int(input("Insira a quantidade de votos nulos:"))
    votos_brancos= int(input("Insira a quantidade de votos em branco:"))


    total_votos= votos_a + votos_b + votos_c + votos_brancos + votos_nulos
    print(f"O número total de eleitores é: {total_votos}")


    perct_votos_a= round((votos_a/total_votos)*100, 1)
    perct_votos_b= round((votos_b/total_votos)*100, 1)
    perct_votos_c= round((votos_c/total_votos)*100, 1)
    perct_votos_nulos= round((votos_nulos/total_votos)*10, 1)
    perct_votos_brancos= round((votos_brancos/total_votos)*100, 1)


    print(f"O percentual de votos do candidato A é: {perct_votos_a} porcento")
    print(f"O percentual de votos do candidato B é: {perct_votos_b} porcento")
    print(f"O percentual de votos do candidato C é: {perct_votos_c} porcento")
    print(f"O percentual de votos nulos é: {perct_votos_nulos} porcento")
    print(f"O percentual de votos em branco é: {perct_votos_brancos} porcento")


if __name__== '__main__':
    exec18()


