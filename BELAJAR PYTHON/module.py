# Belajar Module
#mengambil program dari file modul fuction.py menggunakan "import"
import fuction
hello = fuction.say_hello("khamdan")
print(hello)
hasil = fuction.total(2,5,6,7)
print(hasil)

# cara lain membuat module
from fuction import say_hello
from fuction import total
hello = say_hello ("Emir")
print(hello)
hasil = total (2,4,6,9)
print(hasil)