def exec10():
    num= float(input("Insira um número: "))


    if num>0:
        op_1= round(num/2, 2)
        print(op_1)

    else:
        op_2= round(num**2, 3)
        print(op_2)


if __name__== '__main__':
    exec10()