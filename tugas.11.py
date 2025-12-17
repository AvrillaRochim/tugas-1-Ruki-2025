character = input("masukan karakter: ")
input_jumlah = int(input("masukan jumlah;"))
cetak = " " + character + " "

for i in range (1, input_jumlah + 1):
    spaces = " " * (input_jumlah - i)
    syimbols = character * (2*i-1)
    print(spaces + cetak * i)