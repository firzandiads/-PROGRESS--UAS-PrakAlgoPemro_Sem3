//Firzandi Ahsan Dwi Styana
//21537144016

import java.util.Scanner;

public class Deret3 {
    private static Scanner input;

    public static void main(String args[]) {
    input = new Scanner(System.in);

    int masaKerja;
    double gaji = 3000000.0;

    System.out.print("masukan masa kerja (bulan): ");
    masaKerja = input.nextInt();
    System.out.println();

    System.out.println("Berdasarkan masa kerja, maka");
    if (masaKerja >= 0 && masaKerja <= 6) {
        System.out.println("banyaknya BONUS yang diperoleh = Rp. 0.0");
        System.out.println("Banyaknya THR yang diperoleh Rp"+ String.valueOf(0.5 * gaji));

    }else if (masaKerja > 6 && masaKerja < 12) {
        System.out.println("banyaknya BONUS yang diperoleh =  Rp. 200000.0");
        System.out.println("Banyaknya THR yang diperoleh = Rp" + String.valueOf(1 * gaji));

    }else if (masaKerja >= 12 && masaKerja <= 60) {
        System.out.println("Banyaknya BONUS yang diperoleh = Rp. 300000.0");
        System.out.println("Banyaknya THR yang diperoleh =  Rp" + String.valueOf(1.5 * gaji));

    }else if (masaKerja > 60) {
        System.out.println("Banyaknya BONUS yang diperoleh = Rp. 1000000.0");
        System.out.println("Banyaknya THR yang diperoleh =  Rp" + String.valueOf(2.5 * gaji));

    }else{
        System.out.println("Data Yang Anda Masukkan Salah");

    }
  }
}