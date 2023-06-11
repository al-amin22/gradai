angka = 0.5555
hasil = '{:.2f}'.format(angka*100).replace('.', ',')
print(hasil) # Output: '55,55'


angka = angka / 3
hasil1 = (round(angka * 100,2))


print(hasil1)


angka = 55.234354655456/3
angka_bulat = round(angka, 2)
angka_string = str(angka_bulat)
angka_hasil = angka_string.split('.')
hasil = f"{angka_hasil[0]},{angka_hasil[1]}"
print(hasil)
