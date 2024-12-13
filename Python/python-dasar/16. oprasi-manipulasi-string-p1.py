# operasi dan manipulsi string

# 1. menyambung string (concatenate)
nama_pertama = "Monkey"
nama_tengah = "D"
nama_akhir = "Luffy"

namaLengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(namaLengkap)

# 2. menghitung panjang dari string
panjang = len(namaLengkap)
print("panjang dari " + namaLengkap + "=" + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string 

d = "d"
status = d in namaLengkap
print(d + " Ada di " + namaLengkap + " = " + str(status))

D = "D"
status = D in namaLengkap
print(D + " Ada di " + namaLengkap + " = " + str(status))

d = "d"
status = d not in namaLengkap
print(d + " Ada di " + namaLengkap + " = " + str(status))

# mengulang string
print("wk" * 10)
print(15 * "wk")

# indexing
print("Indeks ke-0 : " + namaLengkap[0])
print("Indeks ke-1 : " + namaLengkap[1])
print("Indeks ke-7 : " + namaLengkap[7])
print("indeks ke-[0:3]:" + namaLengkap[0:6])
print("indeks ke-[7:14]:" + namaLengkap[7:14])
print("indeks ke-[0,2,4,6,8]:" + namaLengkap[0:10:2])

# item paling kecil
print("paling kecil: " + min(namaLengkap))
# item paling besar
print("paling kecil: " + max(namaLengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "Roronoa Zoro"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))