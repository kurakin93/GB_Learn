package org.example.HW.HW1.EX1;

//Given an input string s, reverse the order of the words.
//        A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
//        Return a string of the words in reverse order concatenated by a single space.
//        Note that s may contain leading or trailing spaces or multiple spaces between two words.
//        The returned string should only have a single space separating the words. Do not include any extra spaces.
//        Example 1:
//        Input: s = "the sky is blue"
//        Output: "blue is sky the"

public class Ex1 {
    public static void main(String[] args) {
        String s = "the sky is blue";
        String[] arr = s.split("\\b");

        StringBuilder text_rev = new StringBuilder();
        for (int i = arr.length-1; i >= 0; i--) {
            text_rev.append(arr[i]);
        }
        String reversedString = text_rev.toString();
        System.out.println(reversedString);
    }
    
}