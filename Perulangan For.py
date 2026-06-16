# input nama
nama = input("Masukkan nama anda: ")
 
# nama yang dianggap benar (ganti sesuai kebutuhan)
nama_benar = "denda"  
 
if nama.lower() == nama_benar:
   print("Nama benar, lanjut ke program...\n")
   
   # input angka
   angka = int(input("Masukkan angka (1-10): "))
   
   # validasi angka
   if 1 <= angka <= 10:
       print(f"\nTabel perkalian {angka}:")
       
       # perulangan for
       for i in range(1, 11):
           print(f"{angka} x {i} = {angka * i}")
   else:
       print("Angka harus antara 1 sampai 10")
       
else:
   print("Silahkan coba lagi")