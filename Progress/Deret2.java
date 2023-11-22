//Firzandi Ahsan Dwi Styana
//21537144016

import java.util.Scanner;

public class Deret2 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int i, j, deretDeret;

        System.out.print("Masukkan Banyaknya Deret: ");
        deretDeret = in.nextInt();

        for(i = 1; i <= deretDeret; i++) {
            for(j = 1; j<= i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }

    }
    
}