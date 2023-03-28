package org.example.CW.Lesson_1.Lekc1;

//import static jdk.internal.org.jline.utils.Colors.s;
import java.util.Scanner;
public class program {
    public static void main(String[] args){
        Scanner iScanner = new Scanner(System.in);
        System.out.printf("Name: ");
        boolean flag = iScanner.hasNextInt();
        System.out.println(flag);
        String i = iScanner.nextLine();
        System.out.println(i);
        iScanner.close();
    }
}
