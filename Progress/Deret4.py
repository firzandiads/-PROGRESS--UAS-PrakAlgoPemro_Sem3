#Firzandi Ahsan Dwi Styana
#21537144016

nName = input ("Masukkan nama pegawai: ")
jumlahWaktu = int(input("Masukkan jumlah jam kerja: "))
gGolongan = int(input("Golongan pegawai:"))
sStatus = input("Status pegawai sudah menikah (Y/T) :")
jumlahAnakanak = int(input("Masukkan jumlah anak: "))
besarGajian = 0
bonusLembur = 0 
tunjanganIstri = 0
tunjanganAnak = 0
totalgaji = 0

print("\nBerdasarkan masa kerja, maka")

if jumlahWaktu > 150:
   bonusLembur =+ 300000
else:
    bonusLembur =+ 0
if sStatus == "Y" or sStatus == "y":
    tunjanganIstri =+ 200000
else:
    tunjanganIstri =+ 0

if jumlahAnakanak == 0:
    tunjanganAnak =+ 0
elif jumlahAnakanak == 1:
    tunjanganAnak =+ (1 * 75000)
elif jumlahAnakanak == 2:
    tunjanganAnak =+ (2 * 75000)
else:
    tunjanganAnak =+ (2 * 75000)

if gGolongan == 1:
    besarGajian = (40000 * jumlahWaktu)
    print("Besar gaji: Rp" +str(besarGajian))
    print("Bonus lembur: Rp" + str(bonusLembur))
    print("Tunjangan istri: Rp" + str(tunjanganIstri))
    print("Tunjangan anak: Rp" + str(tunjanganAnak))
    print("\nTotal gaji: Rp" + str(besarGajian + bonusLembur +tunjanganIstri + tunjanganAnak))
    
elif gGolongan == 2:
    besarGajian = (50000 * jumlahWaktu)
    print("Besar gaji: Rp" +str(besarGajian))
    print("Bonus lembur: Rp" + str(bonusLembur))
    print("Tunjangan istri: Rp" + str(tunjanganIstri))
    print("Tunjangan anak: Rp" + str(tunjanganAnak))
    print("\nTotal gaji: Rp" + str(besarGajian + bonusLembur +tunjanganIstri + tunjanganAnak))
    
elif gGolongan == 3:
    besarGajian = (60000 * jumlahWaktu)
    print("Besar gaji: Rp" +str(besarGajian))
    print("Bonus lembur: Rp" + str(bonusLembur))
    print("Tunjangan istri: Rp" + str(tunjanganIstri))
    print("Tunjangan anak: Rp" + str(tunjanganAnak))
    print("\nTotal gaji: Rp" + str(besarGajian + bonusLembur +tunjanganIstri + tunjanganAnak))
    
elif gGolongan == 4:
    besarGajian = (75000 * jumlahWaktu)
    print("Besar gaji: Rp" +str(besarGajian))
    print("Bonus lembur: Rp" + str(bonusLembur))
    print("Tunjangan istri: Rp" + str(tunjanganIstri))
    print("Tunjangan anak: Rp" + str(tunjanganAnak))
    print("\nTotal gaji: Rp" + str(besarGajian + bonusLembur +tunjanganIstri + tunjanganAnak))
    
else:
    print("Data yang anda masukkan salah")