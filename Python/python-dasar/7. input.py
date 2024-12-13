# data yang dimasukkan pasti string
data = input("Masukkan nama: ")

print("data = ", data, ", type: ", type(data))

# jika ingin mengambil int, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))
print("data = ", angka, ", type: ", type(angka))

# bagaimana dengan boolean
biner = bool(int(input("Masukkan nilai biner: ")))
print("data = ", biner, ", type: ", type(biner))