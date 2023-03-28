#Program Management Kontak
import function
#list of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "khamdan" ,
    "email" : "echo.Khamdan@std.unissula.ac.id" ,
    "telepon" : "08985566531"})

#Menu program
while True:
    print("#menu")
    print("1.Daftar Kontak")
    print("2.Tambah kontak")
    print("3.Hapus Kontak")
    print("4.Cari Kontak")
    print("0.Keluar Program")

    menu = input("Pilhan Menu : ")

    if menu == "0":
        break
    elif menu =="1":
        function.display_kontak(daftar_kontak)
    elif menu =="2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu =="3":
        function.hapus_kontak(daftar_kontak)
    elif menu =="4":
        function.hapus_kontak(daftar_kontak)
        

print("Program Selesai Berjalan, Sampai Jumpa")