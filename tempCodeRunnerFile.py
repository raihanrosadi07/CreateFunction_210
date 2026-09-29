
def konversi_suhu(nilai, satuan):
    satuan = satuan.upper()
    if satuan == "C":                    
        return nilai * 9 / 5 + 32
    elif satuan == "F":                  
        return (nilai - 32) * 5 / 9
    else:
        return "Satuan harus 'C' atau 'F'"

print(konversi_suhu(100, "C"))  
print(konversi_suhu(212, "F"))   

luas_lingkaran = lambda r: 3.14 * r ** 2

print(luas_lingkaran(7))       