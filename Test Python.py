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

print("\n{}<================> \t{}Nama Kamu    {}: " .format(rt,gr,rd), nama,"\t\t""<================>", rt)
print("{}<================> \t{}Kelas Kamu   {}: " .format(rt,gr,rd), kelas,"\t\t\t\t""<================>", rt)
print("{}<================> \t{}Jurusan Kamu {}: " .format(rt,gr,rd), jurusan,"\t""<================>\n", rt)
