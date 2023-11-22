data = []
total = 0
totalListVarian = 0
listVarian = []

jumlah_data = int(input('Masukkan jumlah data: '))

for i in range(1, jumlah_data + 1):
    print('Masukkan data ke-', i, '=', end = ' ')
    nilaiData = int(input())
    data.append(        
        nilaiData
    )
    total = total + nilaiData

rerata = total/i

for nilaiData in data:
    nilaiVarian = (nilaiData - rerata) ** 2
    listVarian.append(
        nilaiVarian
    )
    totalListVarian = totalListVarian + nilaiVarian

varian = totalListVarian/i

standarDeviasi = varian ** 0.5

print('\nData\t\t\t=',data)
print('Total data\t\t=',total)
print('Rata-rata\t\t=',rerata)
print('Standar Deviasi data\t=',standarDeviasi)