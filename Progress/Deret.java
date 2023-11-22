//Firzandi Ahsan Dwi Styana
//21537144016

import java.util.Scanner;

class DeretNo1{
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int deretDeret, i;
        int total = 0;

        System.out.print("masukan banyaknya deret: ");
        deretDeret = input.nextInt();

        System.out.println("Tampilkan:");
        for (i = 1; i <= deretDeret; i++) {
            if (i % 2 == 0) {
                System.out.print(i * -1 + " ");
                total += (i * -1);    
            } else {
                System.out.print(i + " ");
                total += i;  
            }
            
        }
        System.out.println();
        System.out.print("jumlah datanya = " + total);
    }
}