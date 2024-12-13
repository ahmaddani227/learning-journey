# latihan date dan time

import datetime as dt


print("Silahkan masukkan tanggal, \nbulan, dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggalLahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggalLahir}")

hariIni = dt.date.today()
print(f"Hari ini tanggal : {hariIni}")
umurHari = hariIni - tanggalLahir
umurTahun = umurHari.days // 365
umurBulanSisa = (umurHari.days % 365) // 30
# print(umurTahun)
print(f"Harinya adalah : {tanggalLahir:%A}")
print(f"Umur anda adalah : {umurTahun} tahun, {umurBulanSisa} bulan")