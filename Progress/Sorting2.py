#Firzandi Ahsan DS
#21537144016

data = [5, 37, 6, 11, 29]
print("Data sebelum disorting : ")
print(data)
	
rentang = len(data) // 2
while rentang > 0:
    for i in range(rentang, len(data)):
        temp = data[i]
        j = i
        
        while j >= rentang and data[j - rentang] < temp:
            data[j] = data[j - rentang]
            j -= rentang
        
        data[j] = temp
    rentang //= 2

print("Data setelah disorting : ")
print(data)