# Belajar Tipe Data Dictionary {}

customer ={'nama':'khamdan','Age':'27','address':'Ungaran'}

nama = customer['nama']
Age = customer['Age']
Address = customer['address']

#for key in customer:
#    value = customer[key]
#    print(f'{key} : {value}')
customer['Company'] = 'PLN Persero'
customer ['nama'] = 'Khamdan Annas Fakhryza'

#menghapus dict yaitu dengan 'del
del customer['Age']

#cara menggunakan dictionary yaitu menggunakan 'items
for key,value in customer.items():
    print(f'{key}:{value}')
