# contoh fungsinya return didalam fungsi : mengembalikan hasil

def luas_persegi_panjang(panjang, lebar):
    hasil = (panjang * lebar)
    print('luas persegi panjang', hasil)

luas_persegi_panjang(2, 4)

#ditambahkan return

def luas_persegi_panjang(panjang, lebar):
    hasil = (panjang * lebar)
    return hasil

teks1 = luas_persegi_panjang(2, 4)
print('luas persegi panjang', teks1)