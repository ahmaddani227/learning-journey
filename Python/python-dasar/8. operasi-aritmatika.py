# operasi aritmatika

a = 10
b = 3

# opertasi tambah
hasil = a + b
print(a, "+", b, "=", hasil)

# opertasi pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

# opertasi perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

# opertasi perpembagian
hasil = a / b
print(a, "/", b, "=", hasil)

# opertasi eksponen(pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# opertasi modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# opertasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioriat operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dkk ** * % / //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(', x, '+', y, ') *', z, '=', hasil)