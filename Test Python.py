#  input data
#  kode warna
rt = '\033[0m'
rd = '\033[31m'
lcy = '\033[96m'
gr = '\033[92m'
mg = '\u001b[35m'
yl = '\033[93m'
lrd = '\033[91m'
pl = '\033[35m'

print("\n[{}!{}]{}\tMasukkan Nama Anda  {}: {}Adam Zafron Zaman               {}[{}!{}] " .format(rd,rt,rd,rt,lcy,rt,rd,rt))
print("[{}!{}]{}\tInput Nama Kelas    {}: {}Mekkah                          {}[{}!{}] " .format(rd,rt,rd,rt,lcy,rt,rd,rt))
print("[{}!{}]{}\tInput Jurusan       {}: {}Pengembangan Perangkat Lunak    {}[{}!{}] " .format(rd,rt,rd,rt,lcy,rt,rd,rt))

nama = input("\n{}[{}?{}]{}\tNama \t{}:{}  " .format(rt,yl,rt,gr,rt,pl))
kelas = input("{}[{}?{}]{}\tKelas \t{}:{}  " .format(rt,yl,rt,gr,rt,pl))
jurusan = input("{}[{}?{}]{}\tJurusan {}:{}  " .format(rt,yl,rt,gr,rt,pl))

# dekorasi
print("\n\n{}{}===================={}      {}Hasil Data{}      {}===================={}\n" .format(rt,rd,rt,lcy,rt,rd,rt))

print("\n{}<================> \t{}Nama Kamu    {}:{} " .format(rt,gr,rt,rd), nama, rt, "\t\t""<================>" )
print("{}<================> \t{}Kelas Kamu   {}:{} " .format(rt,gr,rt,rd), kelas, rt, "\t\t\t""<================>" )
print("{}<================> \t{}Jurusan Kamu {}:{} " .format(rt,gr,rt,rd), jurusan, rt, "\t""<================>\n ")


#  input nilai
# Program make a simple calculator

#  kode warna
rt = '\033[0m'
rd = '\033[31m'
lcy = '\033[96m'
gr = '\033[92m'
mg = '\u001b[35m'
yl = '\033[93m'
lrd = '\033[91m'
pl = '\033[35m'

# This function adds three numbers
def add(x, y, z):
    return x + y + z

# This function subtracts three numbers
def subtract(x, y, z):
    return x - y - z

# This function multiplies three numbers
def multiply(x, y, z):
    return x * y * z

# This function divides three numbers
def divide(x, y, z):
    return x / y / z


# Question 1
print("\n\n[{}!{}]{}\tBerapakah nilai penjumlahan dari bilangan berikut, jika {}x {}={} 250{}, {}y {}={} 250{}, {}z {}={} 250{}!!\t[{}!{}]" .format(rd,rt,gr,rd,rt,rd,rt,lcy,rt,lcy,rt,yl,rt,yl,rt,rd,rt,rt))

# Question 2
print("\n\n[{}!{}]{}\tBerapakah nilai pengurangan dari bilangan berikut, jika {}x {}={} 255{}, {}y {}={} 140{}, {}z {}={} 30{}!!\t[{}!{}]" .format(rd,rt,gr,rd,rt,rd,rt,lcy,rt,lcy,rt,yl,rt,yl,rt,rd,rt,rt))

# Question 3
print("\n\n[{}!{}]{}\tBerapakah nilai perkalian dari bilangan berikut, jika {}x {}={} 2{}, {}y {}={} 4{}, {}z {}={} 5{}!!\t\t[{}!{}]" .format(rd,rt,gr,rd,rt,rd,rt,lcy,rt,lcy,rt,yl,rt,yl,rt,rd,rt,rt))

# Question 4
print("\n\n[{}!{}]{}\tBerapakah nilai pembagian dari bilangan berikut, jika {}x {}={} 81{}, {}y {}={} 9{}, {}z {}={} 3{}!!\t\t[{}!{}]\n\n" .format(rd,rt,gr,rd,rt,rd,rt,lcy,rt,lcy,rt,yl,rt,yl,rt,rd,rt,rt))


# Select Operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        n1 = float(input("Enter first number    :     "))
        n2 = float(input("Enter second number   :     "))
        n3 = float(input("Enter third number    :     "))

        if choice == '1':
            print(n1, "+", n2, "+", n3, "=", add(n1, n2, n3))

        elif choice == '2':
            print(n1, "-", n2, "-", n3, "=", subtract(n1, n2, n3))

        elif choice == '3':
            print(n1, "*", n2, "*", n3, "=", multiply(n1, n2, n3))

        elif choice == '4':
            print(n1, "/", n2, "/", n3, "=", divide(n1, n2, n3))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    
    else:
        print("Invalid Input")
