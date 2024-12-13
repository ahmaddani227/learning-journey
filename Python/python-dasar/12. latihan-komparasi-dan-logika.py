# latihan komparasi dan boolean

# membuat gabungan area rentang dari angka

# +++++++++3---------10+++++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10: "))

# ++++++++3---------------
# memriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(f"Kurang dari 3 = {isKurangDari}")

# ------------10+++++++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print(f"Lebih dari 10 = {isLebihDari}")

# +++++++++3---------10+++++++++
isCorrect = isKurangDari or isLebihDari
print(f"angka yang anda masukkan {isLebihDari}")

# --------3+++++++++10---------
print("\n",'=' * 20,'\n')
# kasus irisan
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10: "))

# ----------3++++++++++++
# lebih dari 3 
isLebihDari = inputUser > 3
print(f"is lebih dari 3 = {isLebihDari}")

# ++++++++++10-----------
# kurang dari
isKurangDari = inputUser < 10
print(f"is kurang dari 10 = {isKurangDari}")

# --------3+++++++++10---------
isCorrect = isKurangDari and isLebihDari
print(f"angka yang anda masukkan {isLebihDari}")


