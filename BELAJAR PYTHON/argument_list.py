# Belajar Argument List

#argumnet list
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f'Total = {list_angka} = {total}')

jumlahkan(30,4,5,8,9)
#print('Penjumlahan')
#data = input('data : ')
#data1 = input('data2 : ')
#data2 = input('data3 : ')

#def jumlahkan(data,data1,data2):
#    total 0
#    for 
#    total = data + data1 +data2
#print(f'TOTAL LIST = {data} + {data1} +{data2}')
