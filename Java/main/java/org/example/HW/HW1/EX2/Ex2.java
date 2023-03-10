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
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int value;
        int sum = 0;
        int count = 0;
        do {
            System.out.println("Input number: ");
            value = scanner.nextInt();
            sum = sum + value;
            if (value < 0){
                System.out.println(sum);
                sum = 0;
            }
        } while (value != 0);
        System.out.println("Input 0");
    }
}




//    public static Integer sumCountPositiveNumb1() {
//        Scanner scanner = new Scanner(System.in);
//        System.out.println("Input number: ");
//        int number_first = scanner.nextInt();
//        int count = number_first;
//        while (number_first != 0) {
//            System.out.println("Input number: ");
//            int number_second = scanner.nextInt();
//            if (number_first > 0 && number_second > 0) {
//                number_first = number_second;
//                count += number_first;
//            }
//            else {
//                if (number_second < 0) {
//                    scanner.close();
//                    return count;
//                }
//            }
//        }
//    }








