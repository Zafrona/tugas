from os import system, name
import random
import string

# Kode Warna
rt = '\033[0m'
rd = '\033[31m'
lcy = '\033[96m'
gr = '\033[92m'
mg = '\u001b[35m'
yl = '\033[93m'
lrd = '\033[91m'
pl = '\033[35m'

# inisiasi fungsi clear terminal
def clear():

    # jika os windows
    if name == 'nt':
        _ = system('cls')

    # jika os mac / linux
    else:
        _ = system('clear')

# Menerima input username min 10 char, no space
def cek_username():
    valid = True
    while valid:
        print("\n\t\t     [!]  Rules   [!]\n[1] Username Harus Menggunakan Huruf Kapital di Awalan!!!\n[2] Username Tidak Boleh Mengandung Spasi!!!\n[3] Panjang Username Minimal 10 Karakter!!!")
        user = input("\nMasukkan Username :   ")
        cek = len(user) >= 10 and " " not in user and user[0].isupper() == True
        status = ""

        if cek:
            status = "[✓]{}  Username Berhasil di Validasi   {}[✓]" .format(gr,rt)
            print(status)
            print()
            valid = False
            return user

        else:
            status = "[✕]{}  Username Tidak Valid    {}[✕]" .format(rd,rt)
            print(status)
            print()

# Menerima input email min 8 char, no space, harus ada @ & .
def cek_email():
    valid1 = True
    while valid1:
        print("\n\t     [!]  Rules   [!]\n[1] Email Tidak Boleh Mengandung Spasi!!!\n[2] Panjang Email Minimal 8 Karakter!!!\n[3] Email Harus Mengandung @ dan .!!!")
        email = input("\nMasukkan Email    :   ")
        cek1 = len(email) >= 8 and "@", "." in email and " " not in email

        if cek1:
            status = "[✓]{}  Email Berhasil di Validasi  {}[✓]" .format(gr,rt)
            print(status)
            print()
            valid1 = False
            return email

        else:
            status = "[✕]{}    Email Tidak Valid   {}[✕]" .format(rd,rt)
            print(status)
            print()

# Menerima input no handphone string angka
def cek_nomer_hp():
    valid2 = True
    while valid2:
        no_hp = input(str("\nMasukkan No.Handphone  :   "))

        if no_hp.isdigit() == True:
            status = "[✓]{}  Nomor Handphone Berhasil di Validasi    {}[✓]" .format(gr,rt)
            print(status)
            print()
            valid2 = False
            return no_hp

        else:
            status = "[✕]{}  Nomor Tidak Valid   {}[✕]" .format(rd,rt)
            print(status)
            print()


def main():
    valid = True
    while valid:
        clear()

        print("")
        print("\t{}██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ ". format(lcy))
        print("\t██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗")
        print("\t██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║")
        print("\t██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║")
        print("\t╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝")
        print("\t ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ {}" . format(rt))
        print("")


        print("")
        print("\t       {}██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗ ██████╗ ██████╗". format(lcy))
        print("\t       ██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
        print("\t       ██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║   ██║██████╔╝")
        print("\t       ╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗")
        print("\t        ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║")
        print("\t         ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{}" . format(rt))
        print("\t")

        username = cek_username()
        emaill = cek_email()
        nohp = cek_nomer_hp()

        print("\n[✓] Username : ", username)
        print("[✓] Email    : ", emaill)
        print("[✓] Nomor    : ", nohp, "\n")

        teks = "Username       :   {}\nEmail          :   {}\nNo.Handphone   :   {}" .format(username, emaill, nohp)
        nama_file = "biodata" + ''.join(random.choice(string.digits) for _ in range(3)) + ".txt"
        file = open(nama_file, "a+")
        file.write(teks)
        file.close()
    
        next_input = input("\n{}{}Buat Akun Lain?(y/n)    :   " .format(rt, rd))
        if next_input == "n":

            print("")
            print("\t{}████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗". format(lcy))
            print("\t╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║")
            print("\t   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║")
            print("\t   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║")
            print("\t   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝")
            print("\t   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ {}" . format(rt))
            print("")                                                                          
            break

main()