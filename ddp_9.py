#1 Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#2 Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
print('\n---- mencari bilangan genap ----')
def is_genap(bil_genap):
    return bil_genap %2 == 0
# Untuk memasukkan value
print(is_genap(4))
print(is_genap(7))

#3 Buatlah fungsi untuk melihat keterangan lulus atau tidak lulus : 
print('\n---- Mencetak nilai kelulusan ----')
def nilai_kelulusan(nilai):
    if nilai >= 70:
        return 'Lulus'
    else :
        return 'Gagal'
    
# untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

#4 Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumen
print('\n---- Cetak Bilangan Genap ----')
def bil_ganjil(angka):
    for i in range(1, angka , 2):
        print(i, end=" ")
# untuk mencetak value
bil_ganjil(20)