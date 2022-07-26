# Program Sederhana Cara Registrasi Akun

#  kode warna
rt = '\033[0m'
rd = '\033[31m'
lcy = '\033[96m'
gr = '\033[92m'
mg = '\u001b[35m'
yl = '\033[93m'
lrd = '\033[91m'
pl = '\033[35m'

print(("{}={}" .format(yl,rt))* 80)
print("\n\t😁{}Selamat Datang di Registrasi Akun Perlu dilindungi Covid-19{}😁\t\n" .format(lcy,rt))
print(("{}={}" .format(yl,rt))* 80)

# Membuat Function 
def register():
    # Membuat Variabel valid dengan kondisi True dan Membuat Perulangan while
    valid = False

    while not valid:

    # Membuat file database.txt agar dapat dibaca oleh programnya dan membuat inputan Username dan Password
        db = open("database.txt", "r")
        pvz = open("data vaksinasi.txt", "r")
        
        Username = input("\n{}Create Username   :   " .format(lcy))
        Password1 = input("{}{}Create Password   :   " .format(rt, lcy))
        Password2 = input("{}{}Confirm Password  :   " .format(rt, lcy))

        # Inisialisasi Variabel d,f sebagai Array kosong untuk wadah 
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        print("\n")
        print(data)

        # p = []
        # v = []
        # z = []
        # for j in pvz:
        #     k,l,m = j.split(", , ")
        #     m = m.strip()
        #     p.append(k)
        #     v.append(l)
        #     z.append(m)
        # datab = dict(zip(p, v, z))
        # print("\n")
        # print(datab)

        
        # Membuat Statement if
        if Password1 != Password2:
            print("\n{}Password tidak sesuai, silahkan coba lagi!!{}" .format(rd,rt))
            register()

        else:
            if len(Password1)<=6:
                print("\n{}Password terlalu pendek, silahkan coba lagi!!{}" .format(rd,rt))
                register()
            
            elif Username in d:
                print("\n{}Username sudah terpakai, silahkan coba lagi!!{}" .format(rd,rt))
                register()
            
            elif Password1 in f:
                print("\n{}Passwor sudah terpakai, silahkan coba lagi!!{}" .format(rd,rt))
                register()
            
            else:
                db = open("database.txt", "a")
                db.write(Username+", "+Password1+"\n" )
                print("\n{}==========|Sukses!!|=========={}" .format(gr,rt))
                print("\n{}Nama Anda    :   " .format(lcy), Username)
                domisili = (input("{}{}Domisili     :    " .format(rt, lcy)))
                vaksin = (input("{}{}Apakah Vaksinasi Terakhir Anda :   " .format(rt, lcy)))
                pvz = open("data vaksinasi.txt", "a")
                pvz.write(Username+", "+domisili+", "+vaksin+"\n" )
                print("\n====|🙏Terimakasih Telah Menggunakan layanan Aplikasi Perlu dilindungi Covid-19🙏|====")
                
                next_input = input("\n{}{}Buat Akun Lain?(y/n)    :   " .format(rt, rd))
                if next_input == "n":
                    print(("{}={}" .format(yl,rt))* 58)
                    print("\n\t🙏{}Terima Kasih Telah Registrasi Akun anda{}🙏\t\n" .format(lcy,rt))
                    print(("{}={}" .format(yl,rt))* 58)
                    print("\n\n\n\n\n\n\n\n")
                    print(("{}={}" .format(yl,rt))* 70)
                    print("\n\t |========== {}No Sweet Without Sweat{} ==========|\n" .format(lcy,rt))
                    print("\t|======= {}Tidak Ada Manis Tanpa Keringat{} =======|\n" .format(lcy,rt))
                    print(("{}={}" .format(yl,rt))* 70)
                    break

# memanggil fungsi 
register()