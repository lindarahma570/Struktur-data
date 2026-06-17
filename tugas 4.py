# Aplikasi Manajemen Nilai Mahasiswa

data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")

    pilihan = input("\nPilih menu 1-8: ")

    if pilihan == "1":
        print("\nDaftar Mahasiswa")
        print("------------------------")
        if len(data_mahasiswa) == 0:
            print("Data masih kosong.")
        else:
            no = 1
            for data in data_mahasiswa:
                print(f"{no}. Nama : {data[0]} | Nilai : {data[1]}")
                no += 1

    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa.append([nama, nilai])
        print("Data berhasil ditambahkan.")

    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data[0] = input("Masukkan nama baru: ")
                data[1] = int(input("Masukkan nilai baru: "))
                ditemukan = True
                print("Data berhasil diubah.")
                break

        if not ditemukan:
            print("Data tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data_mahasiswa.remove(data)
                ditemukan = True
                print("Data berhasil dihapus.")
                break

        if not ditemukan:
            print("Data tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        ditemukan = False

        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                print(f"Nama : {data[0]}")
                print(f"Nilai : {data[1]}")
                ditemukan = True
                break

        if not ditemukan:
            print("Data tidak ditemukan.")

    elif pilihan == "6":
        data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
        print("Data berhasil diurutkan berdasarkan nilai tertinggi.")

    elif pilihan == "7":
        if len(data_mahasiswa) > 0:
            total = 0
            for data in data_mahasiswa:
                total += data[1]

            rata_rata = total / len(data_mahasiswa)
            print(f"Rata-rata nilai mahasiswa = {rata_rata:.2f}")
        else:
            print("Data masih kosong.")

    elif pilihan == "8":
        print("Terima kasih telah menggunakan program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-8.")