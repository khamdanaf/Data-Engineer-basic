# Belajar Method Return Value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total +angka
    #mengembalikan dan menyimpan hasil "total"pada variable
    return(list_angka , total)

list_angka ,total = jumlahkan(10,4,5,6,7)

#mengambil data total?
print(f"Total{list_angka} = {total}")