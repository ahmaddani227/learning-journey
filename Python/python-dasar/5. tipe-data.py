# a = 10, a adalah variable dengan value atau nilai 10

# tipe data: Angka satuan yang tidak ada komanya (Integer)
data_integer = 11
print("data :", data_integer, ", bertipe :", type(data_integer))

# tipe data: Angka dengan koma (Float)
data_float = 11.5
print("data :", data_float, ", bertipe :", type(data_float))

# tipe data: Kumpulan karakter (String)
datat_string = "Ahmad Dani"
print("data :", datat_string, ", bertipe :", type(datat_string))

# tipe data: biner true/false (boolean)
datat_boolean = True
print("data :", datat_boolean, ", bertipe :", type(datat_boolean))


# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("data :", data_complex, ", bertipe :", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.7)
print("data :", data_c_double, ", bertipe :", type(data_c_double))