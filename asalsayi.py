asalsayilar=[2]
kontrolsayisi=3
mod=[]
ustlimit=int(input("Kaça kadar olan asal sayıları bulmak istiyorsunuz\n"))
x=2

while 2*x<ustlimit:
    i=0
    while i<len(asalsayilar):
        mod.append(kontrolsayisi%asalsayilar[i])
        i+=1
        if 0 in mod:
            kontrolsayisi+=2
            mod.clear()
            x+=1
        else:
            continue
    asalsayilar.append(kontrolsayisi)
    kontrolsayisi+=2
    mod.clear()
    x+=1

print(asalsayilar)