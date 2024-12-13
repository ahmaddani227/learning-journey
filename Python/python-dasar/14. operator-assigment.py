# operator assigment
# operasi yang dapat ditambah dengan assigment

a = 5 # ini adalah assigment
print(f"nilai a = {a}")

a += 1 # artinya a = a + 1
print(f"nilai a += 1 menjadi {a}")

a -= 2 # artinya adalah a = a -2
print(f"nilai a += 1 menjadi {a}")

a *= 5 # artinya adalah a = a * 5
print(f"nilai a *= 5 menjadi {a}")

a /= 2 # artinya adalah a = a / 2
print(f"nilai a *= 2 menjadi {a}")

b = 10
print(f"\nNilai b = {b}")

# modulus dan floor division
b %= 3
print(f"nilai a %= 3 menjadi {b}")

b = 10
print(f"\nNilai b = {b}")

b //= 3
print(f"nilai a //= 3 menjadi {b}")

a = 5
print(f"nilai a = {a}")

# pangkat atau eksponen
a **= 3
print(f"nilai a **= 3 menjadi {a}")

# operasi bitwise
# OR
c = True
print(f"Nilai c = {c}")
c |= False
print(f"Nilai c |= False, Nilai c menjadi {c}")
c = False
print(f"Nilai c = {c}")
c |= False
print(f"Nilai c |= False, Nilai c menjadi {c}")

# AND
c = True
print(f"Nilai c = {c}")
c &= False
print(f"Nilai c &= False, Nilai c menjadi {c}")
c = True
print(f"Nilai c = {c}")
c &= True
print(f"Nilai c &= True, Nilai c menjadi {c}")

# XOR
c = True
print(f"Nilai c = {c}")
c ^= False
print(f"Nilai c ^= False, Nilai c menjadi {c}")
c = True
print(f"Nilai c = {c}")
c ^= True
print(f"Nilai c ^= True, Nilai c menjadi {c}")

# geser geser
d = 0b0100
print(f"\nNilai d = {format(d, '04b')}")
d >>= 2
print(f"Nilai d >>= 2, Nilai d menjadi {format(d, '04b')}")
d <<= 1
print(f"Nilai d <<= 1, Nilai d menjadi {format(d, '04b')}")
