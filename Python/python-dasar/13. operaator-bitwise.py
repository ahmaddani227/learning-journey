# operator bitwise, operasi biner atau binery

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print("\n==========OR==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print(f"Nilai b: {b}, binary: {format(b, '08b')}")
print("----------------------------(|)")
print(f"Nilai c: {c}, binary: {format(c, '08b')}")

# bitwise AND(&)
c = a & b
print("\n==========AND==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print(f"Nilai b: {b}, binary: {format(b, '08b')}")
print("----------------------------(&)")
print(f"Nilai c: {c}, binary: {format(c, '08b')}")

# bitwise XOR(^)
c = a ^ b
print("\n==========XOR==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print(f"Nilai b: {b}, binary: {format(b, '08b')}")
print("----------------------------(^)")
print(f"Nilai c: {c}, binary: {format(c, '08b')}")

# bitwise NOT (~)
c = ~ a
print("\n==========NOT==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print("----------------------------(~)") 
print(f"Nilai c: {c}, binary: {format(c, '08b')}")
print("----------------------------(^)")
d = 0b0000001001
e = 0b1111111111
print(f"Nilai : {e ^ d} binery: {format(e^d, '08b')}")

# shifting

# shift right (>>)
c = a >> 1
print("\n==========>>==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print("----------------------------(>>)") 
print(f"Nilai c: {c}, binary: {format(c, '08b')}")

# shift left (<<)
c = a << 1
print("\n==========<<==========")
print(f"Nilai a: {a}, binary: {format(a, '08b')}")
print("----------------------------(<<)") 
print(f"Nilai c: {c}, binary: {format(c, '08b')}")
