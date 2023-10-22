T1=[]
T2=[]
T=[]
x=int(input("ecrit la taille x de deux tableux :"))
for i in range (0,x) :
    y=int(input("ecrit le nombre pour tableau 1 :"))
    T1.append(y)
for i in range (0,x) :
    q=int(input("ecrit le nombre pour tableau 2 :"))
    T2.append(q)
for i in range (0,x) :
    S=T1[i]+T2[i]
    T.append(S)
print("la somme de T1 et T2 est :",T)