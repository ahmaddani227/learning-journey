# operator dictonary

data_dic = {
    'ad': 'adit',
    'sp': 'sopo',
    'jrw': 'jarwo',
}

# panjang dictonary
lendict = len(data_dic)
print(f"panjang dictonary: {lendict}")

# mengecek key exist atau tidak
key = 'ad'
checkkey = key in data_dic
print(f"apakah {key} ada di data_dic: {checkkey}")

# mengakses value (read) dengan get
print(data_dic['ad'])
print(data_dic.get('ad'))
print(data_dic.get('up', 'key tidak ditemukan')) # None - check key dengan message tidak ditemukan

# mengupdate data
data_dic['ad'] = 'dani'
print(data_dic)
data_dic['up'] = 'upin'
print(data_dic)

data_dic.update({'ad': 'adit'})
print(data_dic)
data_dic.update({'ip': 'ipin'}) # jika datanya ada akan diupdate kalo tidak ada maka akan ditambahkan
print(data_dic)

# mendelate data pada dictonary
del data_dic['ip']
print(data_dic)