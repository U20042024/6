x=int(input("ecrire le 1er nombre :"))
y=int(input("ecrire le 2eme nombre :"))
k=0
d=0
for i in range (2,x) :
    if x%i==0 :
        d=d+i
for i in range (2,y) :
    if y%i==0 :
        k=k+i
if d==y and k==x :
    print("les deux nombres sont des amis")
else :
    print("les deux nombres sont pas des amis")