# Belajar List
#membuat list
nama =['emir' , 'KHAMDAN' , 'yumna']

#menambah list
nama.append('Eko')

#membuat indeks
#nama[0]

# mengakses indeks harus ada dalam list 
# kalau tidak ada dalam indeks maka akan eror
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])

#untuk mengetahui berapa jumlah yang ada di list
#len(nama)

print(f'TOTAL LIST = {len(nama)}')

# untuk menghapus data
# (dan harus memperhatikan urutan list data
#  karena bisa jadi mengubah posisi indeks)
#nama.remove("  ")
nama.remove('Eko')

# mengubah data di list
print(nama)
nama[2]= 'Patmi'
print(nama)

 