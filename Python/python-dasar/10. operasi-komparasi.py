# operasi komparasi

# setiap hasil dari komparasi adalah Boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari
print("======Lebih besar dari (>)")
hasil = a > 3
print(f"{a} > 3 = {hasil}")
hasil = b > 3
print(f"{b} > 3 = {hasil}")
hasil = b > 2
print(f"{b} > 2 = {hasil}")

# kurang dari <
print("======Kurang dari (<)")
hasil = a < 3
print(f"{a} < 3 = {hasil}")
hasil = b < 3
print(f"{b} < 3 = {hasil}")
hasil = b < 2
print(f"{b} < 2 = {hasil}")

# lebih dari sama dengan >=
print("======Lebih dari sama dengan(>=)")
hasil = a >= 3
print(f"{a} >= 3 = {hasil}")
hasil = b >= 3
print(f"{b} >= 3 = {hasil}")
hasil = b >= 2
print(f"{b} >= 2 = {hasil}")

# kurang dari sama dengan <=
print("======Kurang dari sama dengan(<=)")
hasil = a <= 3
print(f"{a} <= 3 = {hasil}")
hasil = b <= 3
print(f"{b} <= 3 = {hasil}")
hasil = b <= 2
print(f"{b} <= 2 = {hasil}")

# sama dengan ==
print("======Sama dengan(==)")
hasil = a == 4
print(f"{a} == 4 = {hasil}")
hasil = b == 3
print(f"{b} == 4 = {hasil}")

# tidak sama dengan !=
print("======Tidak sama dengan(!=)")
hasil = a != 4
print(f"{a} != 4 = {hasil}")
hasil = b != 3
print(f"{b} != 4 = {hasil}")

print("======Object identity (is)")
# "is" sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")
hasil = x is y
print(f"x is y = {hasil}")

x = 5 # ini adalah assignment membuat object
y = 6
print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")
hasil = x is y
print(f"x is y = {hasil}")

print("======Object identity (is not)")
# "is" sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")
hasil = x is not y
print(f"x is not y = {hasil}")

x = 5 # ini adalah assignment membuat object
y = 6
print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")
hasil = x is not y
print(f"x is not y = {hasil}")
