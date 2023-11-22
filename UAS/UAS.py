# Import library os untuk membersihkan layar console 
import os 
  
# Class stack 
class Stack: 
    def _init_(self): 
        self.items = [] 

    # Memeriksa apakah stack kosong 
    def isEmpty(self): 
        return self.items == [] 
    # Menambah objek/data ke dalam stack 
    def push(self, item): 
        self.items.append(item) 
    # Mengeluarkan data dari stack 
    def pop(self): 
        return self.items.pop() 
    # Menampilkan objek terakhir dari stack 
    def peek(self): 
        return self.items[len(self.items)-1] 
    # Mehitung panjang stack 
    def size(self): 
        return len(self.items) 

    # Linear Search in Python
    def linearSearch(self, n, x):
        return self.items
      # Going through array sequencially
        for i in range(0, n):
            if (items[i] == x):
                return i
        return -1

        n = len(items)
        result = linearSearch(items, n, x)
        if(result == -1):
            print("Element not found")
        else:
            print("Element found at index: ", result)
        
    # Menu dari aplikasi 
    def mainmenu(self): 
        Menu = 1000 
        while Menu != 0 :  
            print("==========================================") 
            print("|           Perpusatakaan ZACI           |") 
            print("|         Tumpukan buku pada rak         |") 
            print("==========================================") 
            print("1. Pegembalian buku") 
            print("2. Peminjaman buku") 
            print("3. Cek Empty") 
            print("4. Kode buku teratas") 
            print("5. Jumlah buku pada rak") 
            print("6. Urutan buku")
            print("7. Pencarian buku")
            print("=========================") 
            pilihan=str(input(("Silakan masukan pilihan anda: "))) 
            if(pilihan=="1"): 
                
                obj = str(input("Kode buku yang dikembalikan: ")) 
                self.push(obj) 
                print("Buku dengan kode "+obj+" telah dikembalikan") 
                x = input("") 
                for i in range(0, len(obj)):
                    index = obj[i]
                    j=i-1
                    while j >=0 and index < obj[j] :
                        obj[j+1] = obj[j]
                        j -= 1
                    obj[j+1] = index

                print(obj)
            elif(pilihan=="2"): 
                
                print("Buku dengan kode "+self.pop()+" telah dipinjam") 
                x = input("") 
            elif(pilihan=="3"): 
                
                print(self.isEmpty()) 
                x = input("") 
            elif(pilihan=="4"): 
                
                print("Kode buku teratas: "+self.peek()) 
                x = input("") 
            elif(pilihan=="5"): 
                
                print("Jumlah buku pada rak: "+str(self.size())) 
                x = input("") 
            elif(pilihan=="6"):
                
                print("Urutan buku : "+str(self.bubbleSort()))
                x = input("") 
            elif(pilihan=="7"):
                
                print("Pencarian no. buku : "+str(self.linearSearch()))
                x = input("") 
            else: 
                print("Maaf, nomor yang anda masukkan salah")  
  
if __name__ == "_main_": 
    s=Stack() 
    s.mainmenu()