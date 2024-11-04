

def np(nome, idade):
    return {"nome" : nome, "idade":idade}

a = np('Matheus', 27)
b = np("Davi", 18)

l = []
l.append(a)
l.append(b)

for i in l:
    if i["idade"] <= 18:
        print(["nome"])

#------------------------------------------

nd = {"nome" : ["Matheus", "Davi"], "idade" : [27,18]}

for i in range(len(nd["nome"])) : 
    if nd["nome"][i] == "Davi":
        print(nd["idade"][i])


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

lp = [Pessoa("Matheus", 27), Pessoa("Davi", 18)]

print(lp)

for pessoa in lp:
    print(pessoa.nome)