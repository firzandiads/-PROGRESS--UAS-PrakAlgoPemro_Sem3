data=[]
for k in range(0,5):
    data.append(int(input("Masukan angka : ")))
for i in range(0, len(data)):
    index = data[i]
    j=i-1
    while j >=0 and index < data[j] :
        data[j+1] = data[j]
        j -= 1
    data[j+1] = index

print(data)