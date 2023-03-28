# Beljar Elif => else if
#jika memakai if mka akan meng eksekusi program di bawahnya
#jika memakai elif dan else maka tidak akan meng eksekusi program di bawahnya


menu_pilihan = input('Silahkan pilih menu (1-3) : ')

if menu_pilihan == '1':
    print('anda memilih 1')
elif menu_pilihan == '2':
    print('anda memilih 2')
elif menu_pilihan == '3':
    print('anda memilih 3')
else:
    print('pilihan anda tidak tersedia')

if menu_pilihan == "x":
    print('program keluar')


