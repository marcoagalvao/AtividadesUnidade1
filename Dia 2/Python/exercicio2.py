def main():
    vetor = []

    for i in range(10):
        vetor.append(int(input("Digite o elemento %d: " % i)))

    # Inicializa as variáveis antes do loop
    maior = vetor[0]
    menor = vetor[0]
    soma = 0
    contMaior5 = 0

    for i in range(len(vetor)):
        soma += vetor[i]
        if vetor[i] > maior:
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]

        if vetor[i] >= 5:
            contMaior5 += 1

    media = soma / len(vetor)

    print("Maior vetor:", maior)
    print("Menor vetor:", menor)
    print("Soma dos valores do vetor:", soma)
    print("Média do vetor:", media)
    print("Quantidade de valores maior ou igual a 5:", contMaior5)

if __name__ == "__main__":
    main()