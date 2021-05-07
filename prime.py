n =100
liste =[] 
for i in range(2,n):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        liste.append(i)
print(liste)