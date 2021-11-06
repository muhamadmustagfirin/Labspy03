print("Menampilkan bilangan terbesar dari n buah data yang diinput")

max = 0
while True:
    a = int(input("Masukan Bilangan: "))
    if max < a:
        max = a
    if a == 0:
        break
print("bilangan terbesar adalah: ", max)
