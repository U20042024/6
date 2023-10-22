N1=[]
n=[]
S=0
x=int(input("ecrit le nombre des eleves :"))
for i in range (0,x) :
    y=int(input("ecrit la note : "))
    while y<0 or y>20 :
       m=int(input("ecrit les nombres entre 0 et 20 "))
    N1.append(y)
    S=S+y
o=S/x
for i in range (0,x) :
    if N1[i]>o :
        n.append(N1[i])
print("les notes superieurs sont :",n)