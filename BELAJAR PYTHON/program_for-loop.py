# Membuat program menggunakan for-loop,
# list dan range

banyak = int(input('Berapa banyak data?'))

nama= []
umur=[]

for angka in range(0, banyak):
    print(f'Urutan data Ke-{angka}')
    input_nama = input("nama : ")
    input_umur = int(input('umur : '))

nama.append(input_nama)
umur.append(input_umur)


for angka in range(0,len(nama)):
    data_nama = nama[angka]
    data_umur = umur[angka]
    print(f'{nama[angka]} berumur {umur[angka]} tahun')