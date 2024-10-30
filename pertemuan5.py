#1. buat tabel variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, WarnaKendaraan, RodaKendaraan] tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan] tambahkan setelah jenis kendaraan dengan value [merk kendaraan]

#list utama kendaraan
Kendaraan = ["mio", "motor", "200cc", "hitam", "roda 2"]
#mencetak isi dari list kendaraan
print(Kendaraan)
#menambahkan value atau nilai di ujung list (pakai append)()
#proses append 1 (harga kendaraan)
Kendaraan.append("20.000.000")
#proses append 2 (tipe kendaraan)
Kendaraan.append("matic")
#cetak nilai kendaraan setelah perubahan
print(Kendaraan)
#sisipkan nilai untuk tipe kendaraan
Kendaraan.insert(2,"yamaha")
#cetak hasil list akhirnya
print(Kendaraan)


#2. 2. buat program python dengan match case untuk menghitung luas bangun datar : jika pilih 1, maka meghitung luas persegi. jika pilih 2, maka menghitung luas lingkaran. jika pilih 3, maka menghitung luas segitiga. kalau pilihannya tidak ada maka keterangan : salah pilih
pilihan = int(input("""pilih nomor pilihan
                    1. Menghitung Luas Persegi
                    2. Menghitung Luas lingkaran
                    3. Menghitung Luas Segitiga"""))
match pilihan :
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukkan nilai sisi: "))
        luasPersegi = s * s
        print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2: 
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukkan nilai jari-jari"))
        luasLingkaran = pi * r** 2
        print(f"Luas Lingkaran dengan jari-jari {r} adalah {luasLingkaran}")
    case 3:
        print("Menghitung Luas Segitiga")
        alas = int(input("Masukkan nilai alas:"))
        tinggi = int(input("Masukkan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
        print("input tidak valid")