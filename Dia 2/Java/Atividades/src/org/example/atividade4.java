package org.example;

import java.util.Scanner;

public class atividade4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] vetor = new int[6];
        int qtdImpar = 0, somaNumsPar = 0;

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = scanner.nextInt();
        }

        System.out.println();
        System.out.print("• Números pares digitados: ");
        for (int n : vetor) {
            if (n % 2 == 0) {
                System.out.print(" " + n + ", ");
                somaNumsPar += n;
            }
        }
        System.out.println();
        System.out.println("• Soma dos números pares: " + somaNumsPar);
        System.out.print("• Números ímpares digitados: ");
        for (int n : vetor) {
            if (n % 2 == 1) {
                System.out.print(" " + n + ", ");
                qtdImpar++;
            }
        }
        System.out.println();
        System.out.println("• Quantidade de números ímpares: " + qtdImpar);

        scanner.close();
    }
}