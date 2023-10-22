r=[]
n=int(input("ecrire le nombre :"))
d=0
for i in range (1,n+1) :
    if n%i==0 :
        d=d+1
        r.append(i)
print("les diviseurs sont : ",d)
print("les diviseurs de ce nombre sont :",r)
