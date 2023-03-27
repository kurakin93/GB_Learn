package org.example.HW.HW6;

import org.example.HW.HW6.model.Model_laptop;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class HW6_Ex1 {
    /**
     * Задание на дом :
     * • Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. Реализовать в java.
     * • Создать множество ноутбуков.
     * • Написать метод, который будет запрашивать у пользователя критерий (или критерии) фильтрации и выведет ноутбуки, отвечающие фильтру.
     * Критерии фильтрации можно хранить в Map. Например:
     * “Введите цифру, соответствующую необходимому критерию:
     * 1 - ОЗУ
     * 2 - Объем ЖД
     * 3 - Операционная система
     * 4 - Цвет …
     * • Далее нужно запросить минимальные значения для указанных критериев - сохранить параметры фильтрации можно также в Map.
     * • Отфильтровать ноутбуки их первоначального множества и вывести проходящие по условиям.
     */
    public static void main(String[] args) {
        action_selection();
    }

    /**
     * Основное меню программы
     */
    static void action_selection() {
        System.out.println("Меню: \n" +
                "1. Открыть весь список ноутбуков\n" +
                "2. Фильтр ноутбуков: \n");
        Scanner sc = new Scanner(System.in);
        List<Model_laptop> temp = new ArrayList<>();
        Integer num = sc.nextInt();
        String str = sc.nextLine();
        switch (num) {
            case 1: {
                print_laptop(laptop_Database());
                action_selection();
                break;
            }
            case 2: {
                sorting_action_selection();
                break;
            }
            case 3: {
            }

        }
    }

    static void sorting_action_selection() {
        List<Model_laptop> temp = new ArrayList<>();
        System.out.println("Фильтр по: \n" +
                "1. Процессору \n" +
                "2. Размеру экрана: \n" +
                "3. Объему DDR \n" +
                "4. OS \n" +
                "5. Цвету \n" +
                "6. Объему HDD \n" +
                "7. Видеокарте \n" +
                "8. Весу \n" +
                "9. Цене \n");
        Scanner sc = new Scanner(System.in);
        Integer num = sc.nextInt();
        String str = sc.nextLine();
        switch (num) {
            case 1: {
                temp = sorting_processor_model(laptop_Database());
                print_laptop(temp);
                break;
            }
            case 2: {
                sorting_screen_size(laptop_Database());
                break;
            }
            case 3: {
                sorting_amount_of_memory(laptop_Database());
            }
            case 4: {
                sorting_operating_system(laptop_Database());
            }
            case 5: {
                sorting_color(laptop_Database());
            }
            case 6: {
                sorting_drive_capacity(laptop_Database());
            }
            case 7: {
                sorting_graphics_card_model(laptop_Database());
            }
            case 8: {
                sorting_weight(laptop_Database());
            }
            case 9: {
                sorting_price(laptop_Database());
                break;
            }
        }
    }

    static List<Model_laptop> laptop_Database() {
        Model_laptop laptop0 = new Model_laptop("amd fx-8350", 15, "ddr5 8 Gb", "Windows", "red", 512, "GeForce", 1245, 9832);
        Model_laptop laptop1 = new Model_laptop("amd ryzen 5", 16, "ddr5 10 Gb", "Windows", "green", 750, "AMD", 1564, 7914);
        Model_laptop laptop2 = new Model_laptop("amd ryzen 3", 17, "ddr5 6 Gb", "Windows", "black", 256, "GeForce", 897, 8946);
        Model_laptop laptop3 = new Model_laptop("amd athlon", 18, "ddr5 12 Gb", "Linux", "orange", 1000, "GeForce", 3212, 9874);
        Model_laptop laptop4 = new Model_laptop("amd phenom", 19, "ddr5 16 Gb", "Linux", "blue", 1500, "AMD", 6547, 1497);
        Model_laptop laptop5 = new Model_laptop("amd sempron", 20, "ddr5 32 Gb", "Apple Mac OS X", "grey", 256, "AMD", 2414, 9879);
        Model_laptop laptop6 = new Model_laptop("intel core i3", 15, "ddr5 4 Gb", "Windows", "yellow", 128, "GeForce", 3215, 4561);
        Model_laptop laptop7 = new Model_laptop("intel core i5", 16, "ddr5 8 Gb", "Apple Mac OS X", "white", 500, "AMD", 3218, 1974);
        Model_laptop laptop8 = new Model_laptop("intel pentium ", 17, "ddr5 16 Gb", "Linux", "red-black", 256, "GeForce", 1564, 3164);
        Model_laptop laptop9 = new Model_laptop("intel celeron", 18, "ddr5 32 Gb", "Apple Mac OS X", "red", 512, "GeForce", 1597, 1567);
        Model_laptop laptop10 = new Model_laptop("intel xeon", 19, "ddr5 36 Gb", "Windows", "black", 512, "AMD", 8923, 66);
        List<Model_laptop> model_laptop = new ArrayList<>();
        model_laptop.add(laptop0);
        model_laptop.add(laptop1);
        model_laptop.add(laptop2);
        model_laptop.add(laptop3);
        model_laptop.add(laptop4);
        model_laptop.add(laptop5);
        model_laptop.add(laptop6);
        model_laptop.add(laptop7);
        model_laptop.add(laptop8);
        model_laptop.add(laptop9);
        model_laptop.add(laptop10);
        return model_laptop;
    }

    static void print_laptop(List<Model_laptop> model_laptop) {
        for (Model_laptop elem : model_laptop) {
            System.out.println(elem);
        }
    }

    static List<Model_laptop> sorting_processor_model(List<Model_laptop> model_laptop) {
        List<Model_laptop> temp = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите модель процессора: ");
        String processor_model = sc.nextLine();
        for (Model_laptop elem : model_laptop) {
            if (compare(elem.getProcessor_model(), processor_model)) {
               temp.add(elem);
            }
        }
        return temp;
    }

    static void sorting_screen_size(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите размер дисплея: ");
        Integer screen_size = sc.nextInt();
        for (Model_laptop elem : model_laptop) {
            if (elem.getScreen_size() == screen_size) {

            }
        }
    }

    static void sorting_amount_of_memory(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите объем DDR: ");
        String amount_of_memory = sc.nextLine();
        for (Model_laptop elem : model_laptop) {
            if (compare(elem.getAmount_of_memory(), amount_of_memory)) {

            }
        }
    }

    static void sorting_operating_system(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите OS: ");
        String operating_system = sc.nextLine();
        for (Model_laptop elem : model_laptop) {
            if (compare(elem.getOperating_system(), operating_system)) {

            }
        }
    }

    static void sorting_color(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите цвет: ");
        String color = sc.nextLine();
        for (Model_laptop elem : model_laptop) {
            if (compare(elem.getColor(), color)) {

            }
        }
    }

    static void sorting_drive_capacity(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите объем HDD: ");
        Integer drive_capacity = sc.nextInt();
        for (Model_laptop elem : model_laptop) {
            if (elem.getDrive_capacity() == drive_capacity) {

            }
        }
    }

    static void sorting_graphics_card_model(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите модель видеокарты: ");
        String graphics_card_model = sc.nextLine();
        for (Model_laptop elem : model_laptop) {
            if (compare(elem.getGraphics_card_model(), graphics_card_model)) {

            }
        }
    }

    static void sorting_weight(List<Model_laptop> model_laptop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите вес: ");
        Integer weight = sc.nextInt();
        for (Model_laptop elem : model_laptop) {
            if (elem.getWeight() == weight) {

            }
        }
    }

    static List<Model_laptop> sorting_price(List<Model_laptop> model_laptop) {
        List<Model_laptop> temp = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите цену: ");
        Integer price = sc.nextInt();
        for (Model_laptop elem : model_laptop) {
            if (elem.getPrice() == price) {
                System.out.println(elem.getPrice());
            }
//            else
//                System.out.println("Такой цены нет! Введите опять.");
//                sorting_price(laptop_Database());

        }
        return temp;
    }

    static List<Model_laptop> temp(Model_laptop elem) {
        List<Model_laptop> temp = new ArrayList<>();
        temp.add(elem);
        return temp;
    }

    static boolean compare(String stringname, String string) {
        return stringname.contains(string);
    }
    static boolean compareInt(Integer integerName, Integer integer) {
        return integerName.equals(integer);
    }
}

