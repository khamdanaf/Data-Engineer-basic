# Belajar Default Argument value

#default parameter tidak wajib memasukkan data para meternya
def say_hello(nama_depan='khamdan', nama_akhir='Annas'):
    print(f'assalamualaikum {nama_depan} {nama_akhir}')
say_hello('Nama Saya')
say_hello( nama_akhir='Emirkhan' , nama_depan='fakhry')
