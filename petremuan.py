import calendar
print("Program menghitung jumlah hari dalam satu bulan")
ulang = "yes"
while ulang == "yes" or ulang == "no": 
    year = int(input("Masukan Tahun : ")) 
    month = int(input("Masukan Bulan : "))
    print("Ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke",month)
    ulang = input("ketik 'yes' untuk lanjut, ketik 'no' untuk stop ")
    if ulang == "no":
        print("Terimakasih sudah Menggunakan program ini")
        print("Jannathan Gerald 065002200016")
        break