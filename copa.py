totEspacos = int(input("digite a quantidade de espaços: "))
figCompradas = int(input("digite a quantidade de figurinhas compradas: "))
figurinhasCompradas = set()

for figurinhas in range(figCompradas):
    fig = int(input("Digite as figurinhas: "))
    figurinhasCompradas.add(fig)

faltam = totEspacos - len(figurinhasCompradas)

print(faltam)
