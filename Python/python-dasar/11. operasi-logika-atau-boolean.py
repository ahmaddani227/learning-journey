# opersi logika atau boolean

# not, or, and, xor

print("=====NOT=====")
a = False
b = not a
print(f"data a = {a}")
print("-----------NOT")
print(f"data b = {b}")

# or (jika salah satu True maka hasilnya adalah True)
print("=====OR=====")
a = False
b = False
c = a or b
print(f"{a} OR {b} = {c}")
a = False
b = True
c = a or b
print(f"{a} OR {b}  = {c}")
a = True
b = False
c = a or b
print(f"{a}  OR {b} = {c}")
a = True
b = True
c = a or b
print(f"{a}  OR {b}  = {c}")

# AND (jika salah satu False maka hasilnya adalah False)
print("=====AND=====")
a = False
b = False
c = a and b
print(f"{a} AND {b} = {c}")
a = False
b = True
c = a and b
print(f"{a} AND {b}  = {c}")
a = True
b = False
c = a and b
print(f"{a}  AND {b} = {c}")
a = True
b = True
c = a and b
print(f"{a}  AND {b}  = {c}")

# XOR (akan true jika salah satu true sisanya false)
print("=====XOR=====")
a = False
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")
a = False
b = True
c = a ^ b
print(f"{a} XOR {b}  = {c}")
a = True
b = False
c = a ^ b
print(f"{a}  XOR {b} = {c}")
a = True
b = True
c = a ^ b
print(f"{a}  XOR {b}  = {c}")