import math

# Soal 1:
def konversi_suhu(nilai, satuan):
    if satuan.upper() == 'C':
        return (nilai * 9 / 5) + 32
    elif satuan.upper() == 'F':
        return (nilai - 32) * 5 / 9
    else:
        return "Satuan tidak valid, gunakan 'C' atau 'F'"

# Soal 2:
luas_lingkaran = lambda r: math.pi * r ** 2


print(konversi_suhu(100, 'C'))  
print(konversi_suhu(212, 'F'))   
print(luas_lingkaran(7))          