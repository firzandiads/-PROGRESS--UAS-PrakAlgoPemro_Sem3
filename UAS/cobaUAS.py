for k in range(0,5):
    items.append(int(input("Kembalikan buku : ")))
for i in range(0, len(items)):
    index = items[i]
    j=i-1
    while j >=0 and index > items[j] :
        items[j+1] = items[j]
        j -= 1
    items[j+1] = index

print(items)