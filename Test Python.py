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
#  kode warna
rt = '\033[0m'
rd = '\033[31m'
lcy = '\033[96m'
gr = '\033[92m'
mg = '\u001b[35m'
yl = '\033[93m'
lrd = '\033[91m'
pl = '\033[35m'


print("\n\n[{}!{}]{}\tBerapakah nilai pembagian dari bilangan berikut, jika {}x {}={} 81{}, {}y {}={} 9{}, {}z {}={} 3{}!!\t[{}!{}]" .format(rd,rt,gr,rd,rt,rd,rt,lcy,rt,lcy,rt,yl,rt,yl,rt,rd,rt,rt))

x = eval(input("\n{}[{}?{}]{}\tx \t{}={} " .format(rt,yl,rt,rd,rt,rd))) 
y = eval(input("{}[{}?{}]{}\ty \t{}={} " .format(rt,yl,rt,lcy,rt,lcy))) 
z = eval(input("{}[{}?{}]{}\tz \t{}={} " .format(rt,yl,rt,yl,rt,yl))) 

# dekorasi
print("\n\n{}{}===================={}      {}Hasil Data{}      {}===================={}\n" .format(rt,rd,rt,lcy,rt,rd,rt))

print ("\n{}<===============> \t{}Hasil dari Pembagian {}x{},{}y{},{}z{} adalah {}" .format(rt,gr,rd,rt,lcy,rt,yl,rt,gr), (x / y / z), rt,  " <===============>\n " )
