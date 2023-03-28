# Belajar Module

def say_hello (nama):
    return f"Halo {nama}"

def total(*list_angka):
    hasil=0
    for data in list_angka:
        hasil = hasil+data
    return hasil

hello = say_hello ("khamdan")
print(hello)
hasil = total(2,5,6,7)
print(hasil)