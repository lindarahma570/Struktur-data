# Input nama
nama = input("Masukan nama anda: ")

# Cek nama (contoh: jika nama tidak kosong dianggap benar)
if nama.strip() != "":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")

# Input umur
umur = int(input("Masukan umur anda: "))

# Percabangan umur
if umur >= 18 and umur <= 60:
    print("Anda cukup umur")
elif umur < 18 and umur > 0:
    print("Anda belum cukup umur")
elif umur <= 0:
    print("Anda belum lahir")
elif umur > 60:
    print("Banyakin ibadah, bentar lagi mati")

print("Program selesai")