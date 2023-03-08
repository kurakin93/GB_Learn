package org.example.HW.HW1.EX2;

import java.util.Scanner;

/**
 * 2) Дана последовательность целых чисел, оканчивающаяся нулем.
 * Найти сумму положительных чисел, после которых следует отрицательное число.
 * Пример ввода:
 * 1 2 1 2 -1 1 3 1 3 -1 0
 * Логика расчета:
 * 2 -1 переход -> 2 в сумму
 * 3 -1 переход -> 3 в сумму
 * Пример вывода: 5
 */

public class Ex2 {
    public static void main(String[] args){
        System.out.println(sumCountPositiveNumb());
    }
    public static Integer sumCountPositiveNumb(){
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("Input second number: ");
        int number = iScanner.nextInt();
        int count = 0;
        while (true) {
            System.out.print("Input first number: ");
            int two = iScanner.nextInt();
            if (two == 0) {
                iScanner.close();
                return count;
            } else {
                if (number > 0 && two < 0) {
                    count += number;
                }
                number = two;
            }
        }

    }
}
