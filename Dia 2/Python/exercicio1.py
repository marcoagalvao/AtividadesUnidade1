def main():
    vetor = [0] * 8

    for i in range(8):
        vetor[i] = int(input(f"Digite o valor da posição {i}: "))

    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    if x < 0 or x >= len(vetor):
        print("Valor de X fora dos limites do vetor.")
        return

    if y < 0 or y >= len(vetor):
        print("Valor de Y fora dos limites do vetor.")
        return

    soma = vetor[x] + vetor[y]

    print(f"A soma dos valores nas posições {x} e {y} é {soma}.")

if __name__ == "__main__":
    main()
