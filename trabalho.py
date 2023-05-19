idadeCibele = int(input("digite a idade de Cibele: "))
idadeCamila = int(input("digite a idade de Camila: "))
idadeCeleste = int(input("digite a idade de Celeste: "))

ordenar = sorted([idadeCibele,idadeCamila,idadeCeleste])

irmaDoMeio = ordenar[1]
irmaMaisNova = ordenar[0]
irmaMaisVelha = ordenar[2]

print(f"a irmã do meio é: {irmaDoMeio}")
print(f"a irmã mais nova é: {irmaMaisNova}")
print(f"a irmã mais velha é: {irmaMaisVelha}")
