# format string

# string
nama = "marlena" 
formatStr = f"hello {nama}"
print(formatStr)

# boolean
boolean = True
formatStr = f"Boolean = {boolean}"
print(formatStr)

# angka 
angka = 2007
formatStr = f"angka = {angka}"
print(formatStr)

# bilangan bulat 
angka = 15
formatStr = f"bilangan bulat = {angka:d}"
print(formatStr)

# bilangan 
angka = 2000000
formatStr = f"ribuan = {angka:,}"
print(formatStr)

# bilangan desimal
angka = 2005.54321
formatStr = f"desimal = {angka:.2f}"
print(formatStr)

# menampilkan leading zero
angka = 2005.54321
formatStr = f"desimal = {angka:08.2f}"
print(formatStr)

# menampilkan tanda + dan -
angkaMinus = -10
angkaPlus = 10
formatMinus = f"Minus = {angkaMinus}"
formatPlus = f"Minus = {angkaPlus:+d}"
print(formatMinus)
print(formatPlus)

# memformat persen %
persentase = 0.045
formatPersen = f"format persen = {persentase:.2%}"
print(formatPersen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
formatString = f"harga total = Rp. {harga * jumlah:,}"
print(formatString)

# format angka lain (binary, octal, hexadecimal)
angka = 255
formatBinary = f"Binary = {bin(angka)}" 
formatOctal = f"Octal = {oct(angka)}"
formatHex = f"Hex = {hex(angka)}"
print(formatBinary)
print(formatOctal)
print(formatHex)