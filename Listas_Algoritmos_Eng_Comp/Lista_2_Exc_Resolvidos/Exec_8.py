def exec8():
    num_1= int(input("Insira o primeiro número inteiro: "))
    num_2= int(input("Insira o segundo número inteiro: "))
    num_3= int(input("Insira o terceiro número inteiro: "))


    if num_1<num_2 and num_2<num_3:
        print(f"Os números em ordem crescente são: {num_1}, {num_2}, {num_3}")


    elif num_1<num_3 and num_3<num_2:
        print(f"Os números em ordem crescente são: {num_1}, {num_3}, {num_2}")


    elif num_2<num_1 and num_1<num_3:
        print(f"Os números em ordem crescente são: {num_2}, {num_1}, {num_3}")


    elif num_2<num_3 and num_3<num_1:
        print(f"Os números em ordem crescente são: {num_2}, {num_3}, {num_1}")


    elif num_3<num_1 and num_1<num_2:
        print(f"Os números em ordem crescente são: {num_3}, {num_1}, {num_2}")


    elif num_3<num_2 and num_2<num_1:
        print(f"Os números em ordem crescente são: {num_3}, {num_2}, {num_1}")


    else:
        print(f"Os números em ordem crescente são: {num_1}, {num_2}, {num_3}")


if __name__== '__main__':
    exec8()