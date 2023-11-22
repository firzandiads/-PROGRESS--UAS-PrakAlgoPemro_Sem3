data = []
total = 0

jumlah_data = int(input('Masukkan jumlah data (maks 20) : '))

if jumlah_data < 21:
    for i in range(1, jumlah_data + 1):
        print('Masukkan data ke-', i, '=', end = ' ')
        nilaiData = int(input())
        data.append(        
            nilaiData
        )
        total = total + nilaiData
else:
    print('Jumlah data yang Anda masukkan salah')
    exit()

print('\nTotal jumlah data  =', total)

ratarata = total / i
print('Rata-ratanya\t    =', ratarata)

print('\n================')
print(' data\t  selisih ')
print('================')
data.sort()
for nilaiData in data:
    selisih = nilaiData - ratarata
    print(f'{nilaiData:>4}\t  {round(selisih, 2):>6}')
print('================')