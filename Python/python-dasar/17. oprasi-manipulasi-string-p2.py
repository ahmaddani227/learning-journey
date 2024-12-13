# operasi string dengan menggunakan method

# merubah case dari string

# merubah semua ke upper case
anime = "one piece"
print("normal: " + anime)

anime = anime.upper()
print("upper: " + anime)

anime = "One Piece"
print("normal: " + anime)
anime = anime.lower()
print("lower: " + anime)

# pengecekan menggunakan isX method
# contoh untuk pengecekan lower case
anime = "naruto"
apakah_lower = anime.islower() # hasilnya bool
print(anime + " is lower = " + str(apakah_lower))
apakah_upper = anime.isupper() # hasilnya bool
print(anime + " is upper = " + str(apakah_upper))

# isalpha() -> untuk mengecek semuanya huruf 
# isalnum() -> huruf dan angka
# isdecimal() -> angka saja
# isspace() -> spasi, tab, newline \n
# istitle() -> semua kata dimulai dengan huruf besar

anime = "Jujutsu Kaisen"
cekAnime = anime.istitle() # hasil bool
print(anime + " is title = " + str(cekAnime))


# ngecek komponen startswith() endswith() <-- keren
cekStart = "Kagurabachi".startswith("Kagurabachi")
print("start = " + str(cekStart))
cekEnd = "Kagurabachi Anime".endswith("Anime")
print("end = " + str(cekEnd))

# penggabungan komponen join(), split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print(5 * "=" + "data" + "=" * 5)

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, "-")
print("'" + tengah + "'")

# kebalikan -> strip()
tengah = tengah.strip("-") # menghilangkna tanda - 
print("'" + tengah + "'")