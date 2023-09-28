# Objetivo: fazer a leitura de duas notas e calcular sua média

# Versão sem modularização
n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))

med = (n2 + n1) / 2

print("Média final:", med)


# Utilizando modularização (utiliza-se funções e procedimentos).
def calcular_media(n1, n2):
    return (n1 + n2) / 2


def obter_notas():
    n1 = float(input("Informe a nota 1: "))
    n2 = float(input("Informe a nota 2: "))
    return n1, n2


n1, n2 = obter_notas()
media_calculada = calcular_media(n1, n2)
print("Média final:", media_calculada)
