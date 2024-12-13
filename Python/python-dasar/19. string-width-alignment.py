# string width dan alignment

# data 
dataNama = "Monkey D Lufy"
dataUmur = 19
dataTinggi = 170
dataSepatu = 38

# string standar
dataString = f"nama = {dataNama}, umur = {dataUmur}, tinggi = {dataTinggi}, sepatu = {dataSepatu}"
print(5*"=" + "Data string" + 5 * "=")
print(dataString)

# string multiline
dataString = f"nama = {dataNama},\numur = {dataUmur}, \ntinggi = {dataTinggi}, \nsepatu = {dataSepatu}"
print("\n"+ 5*"=" + "Data string" + 5 * "=")
print(dataString)

# string multiline (kutip triplets)
dataString = f"""nama = {dataNama},
umur = {dataUmur},
tinggi = {dataTinggi},
nomor sepatu = {dataSepatu}
"""
print("\n"+ 5*"=" + "Data string" + 5 * "=")
print(dataString)

# mengatur lebar
dataNama  = "Luffy"
dataString = f"""
nama         = {dataNama:>5},
umur         = {dataUmur:>5},
tinggi       = {dataTinggi:>5},
nomor sepatu = {dataSepatu:>5}
"""
print("\n"+ 5*"=" + "Data string" + 5 * "=")
print(dataString)