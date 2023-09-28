package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] vetor = new int[8];

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = scanner.nextInt();
        }

        System.out.print("Digite o valor de X: ");
        int x = scanner.nextInt();

        if (x < 0 || x >= 8) {
            System.out.print("X deve estar entre 0 e 7. Insira novamente: ");
            x = scanner.nextInt();
        }

        System.out.print("Digite o valor de Y: ");
        int y = scanner.nextInt();

        if (y < 0 || y >= 8) {
            System.out.print("Y deve estar entre 0 e 7. Insira novamente: ");
            y = scanner.nextInt();
        }

        System.out.println("Soma dos valores nas posições X e Y: " + (vetor[x] + vetor[y]));

        scanner.close();
    }
}