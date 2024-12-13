# Latihan konversi satuan temperature

# program konversi ke satauan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam celcius: '))
print(f"Suhu adalah {celcius} Celcius")

# reamur
reamur = (4/5) * celcius
print(f"Suhu dalam reamur adalah {reamur} Reamur")

# fahrenheit 
fahrenheit = ((9/5) * celcius) * 32
print(f"Suhu dalam Fahrenheit adalah {fahrenheit} Fahrenheit")

# kelvin
kelvin = celcius + 273
print(f"Suhu dalam Kelvin adalah {kelvin} kelvin")