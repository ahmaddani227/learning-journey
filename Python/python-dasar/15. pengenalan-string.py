data = "Ini adala string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan mengunakan single quote '...'
    2. dengan menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"Halo apa kabar ?"')
print("'Halo apa kabar ?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari sholat jum\'at')

# backslash
print("C:\\user\\Dani")

# tab
print("aku\tkamu, jauhan")

# backspace
print("aku \bkamu, jadi deketan")

# newnline
print("Baris pertama.\nBaris kedua") # LF -> line feed
print("Baris pertama.\rBaris kedua") # CR -> cerriage return
print("Baris pertama.\r\nBaris kedua") # CRLF -> line feed carriage return

# 3. Strin literal atau raw
# hati-hati
print("C:\new folder") # akan salah path nya

# menggunkan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Dani
Kelas: A
""")

# multiline literal string dan raw
print(r"""
Nama : Dani
Kelas: A
Github: github.com/ahmaddani227
""")