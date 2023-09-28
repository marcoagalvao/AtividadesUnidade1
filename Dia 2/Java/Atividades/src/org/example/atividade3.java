package org.example;

import java.util.Scanner;

public class atividade3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] vetorA = new int[10];
        int[] vetorB = new int[10];
        int[] vetorC = new int[10];

        for (int i = 0; i < vetorA.length; i++) {
            System.out.print("Digite o valor do vetor A na posição " + i + ": ");
            vetorA[i] = scanner.nextInt();

            System.out.print("Digite o valor do vetor B na posição " + i + ": ");
            vetorB[i] = scanner.nextInt();

            vetorC[i] = vetorA[i] + vetorB[i];
        }

        System.out.println();
        System.out.println("Resultado da soma do vetor A + vetor B: ");
        for (int j = 0; j < vetorC.length; j++) {
            System.out.print(" " + vetorC[j] + ", ");
        }

        scanner.close();
    }
}