package org.example;

import java.util.Scanner;

public class atividade2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] vetor = new int[10];
        int maiorValor = Integer.MIN_VALUE;
        int menorValor = Integer.MAX_VALUE;

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = scanner.nextInt();

            maiorValor = Math.max(maiorValor, vetor[i]);
            menorValor = Math.min(menorValor, vetor[i]);
        }

        System.out.println();
        System.out.println("Maior valor: " + maiorValor);
        System.out.println("Menor valor: " + menorValor);

        scanner.close();
    }
}