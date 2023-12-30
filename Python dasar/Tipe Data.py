# Tipe data : Integer(gk ada komanya)
data_integer = 1
print("data : ", data_integer, ", bertipe : ", type(data_integer))
print("data : ", data_integer)

# tipe data float : angka dgn koma
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))


# tipe data string (kumpulan karakter)
data_string = "ucup 10"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data boolean biner true false
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data khsuusus

#bil kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dr bahasa C

from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-bertipe : ", type(data_c_double))

