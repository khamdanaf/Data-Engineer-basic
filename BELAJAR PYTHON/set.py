# Belajar Set
#

#list => [] data bisa sama
#tuple => () data bisa sama
#set => {} data kalau sama dihapus otomatis
#penambahan nama tidak menggunakan appen tetapi menggunakan add
nama = {"khamdan","yumna","Emir","emir","yumna"}
nama.add("Fakhry")

for data in nama:
    print(data)

nama.remove("emir")

print(nama)