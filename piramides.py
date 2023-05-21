def atividadeExemplo():

    degraus = int(input("Degraus: "))
    k = 0
    for i in range(1, degraus+1):
        for space in range(1, (degraus-i)+1):
            print(end=" ")
        while k != (2*i-1):
            print("*", end="")
            k += 1
        k = 0
        print()

def atividade1():

    degraus = int(input("Degraus: "))
    k = 0
    for i in range(1, degraus+1):
        for space in range(1, (degraus-i)+1):
            print(end=" ")
        while k != (2*i-1):
            print(i, end="")
            k += 1
        k = 0
        print()

def atividade2():

    degraus = int(input("Degraus: "))
    k = 0
    for i in range(1, degraus+1):
        for space in range(1, (degraus-i)+1):
            print(end=" ")
        while k != (2*i-1):
            print(k, end="")
            k += 1
        k = 0
        print()

def atividade3():

    degraus = int(input("Degraus: "))
    k = 0
    for i in range(degraus):
        linha = ""
        for space in range(i+1):
            linha += str(space)
        for k in range(i-1, -1, -1):
            linha += str(k)
        print(linha.center(degraus*2))

def atividade4():

    degraus = int(input("Degraus: "))
    k = 0
    for i in range(1, degraus+1):
        for space in range(1, (degraus-i)+1):
            print(end=" ")
        while k != (2*i-1):
            print(degraus - i, end="")
            k += 1
        k = 0
        print()

atividadeExemplo()
atividade1()
atividade2()
atividade3()
atividade4()