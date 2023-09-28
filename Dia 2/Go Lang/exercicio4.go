package main

import (
	"fmt"
)

func main() {
	var numero, somaPares, quantidadeImpares int
	var numerosPares []int
	var numerosImpares []int

	for i := 1; i <= 6; i++ {
		fmt.Printf("Digite o %dº número inteiro: ", i)
		fmt.Scan(&numero)

		if numero%2 == 0 {
			numerosPares = append(numerosPares, numero)
			somaPares += numero
		} else {
			numerosImpares = append(numerosImpares, numero)
			quantidadeImpares++
		}
	}

	fmt.Println("Números pares digitados:", numerosPares)
	fmt.Println("Soma dos números pares digitados:", somaPares)
	fmt.Println("Números ímpares digitados:", numerosImpares)
	fmt.Println("Quantidade de números ímpares digitados:", quantidadeImpares)
}