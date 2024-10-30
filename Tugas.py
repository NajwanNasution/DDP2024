#Soal 1
#Buatlah variabel list dengan value :[Nama Kendaraan, Jenis Kendaraan, CC Kendaraan, Warna Kendaraan, Roda Kendaraan]
kendaraan = ['Yamaha Mio', 'Sepeda Motor', 200, 'Biru', 2]
print("kendaraan saya")
print(kendaraan)
print("==========")
#Tambahkan Dari Lis Tersebut Di Belakang Dengan Value :[Harga Kendaraan, Tipe Kendaraan]
kendaraan.append(30000000)
kendaraan.append("Matic")
print(kendaraan)
print("==========")
#Tambahkan Setelah Jenis Kendaraan Dengan Value :[Merk Kendaraan]
kendaraan.insert(2, 'Yamaha')
print(kendaraan)
print("==========")

#Soal 2
#Buatlah Program  Python Dengan Macth Case Untuk Menghitung Luas Bangun Datar :
print('Ini adalah program sederhana untuk menghitung lus bangun datar')
print('Pilih menu angka 1-3 : \n1. persegi\n2. lingkaran\n3. segitiga')
pilihmenu = int(input('Silahkan pilih menu dengan mengetikan angka 1-3 : '))
match pilihmenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukkan nilai yang mau dihitung: "))
        hitung = sisi * sisi 
        print("Luas persegi adalah : ", hitung)
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkaran")
        phi = 22/7
        r = int(input('Silahkan masukkan nilai jari-jari: '))
        hitung = phi * r * r
        print("Luas lingkaran adalah : ", hitung)
    case 3:
        print("Ini adalah menu untuk menghitung luas segitiga")
        alas = int(input('Silakan masukkan nilai alas : '))
        tinggi = int(input('silahkan masukkan nilai tinggi : '))
        hitung = 1/2 * alas * tinggi
        print("Luas segitiga adalah: ", hitung)
    case _:
        print("Pilihan tidak valid, silahkan pilih antara 1-3")