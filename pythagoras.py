#a+b+c=1000
#a2+b2 = c2
#a<b<c
a,b,c=None,None,None
for i in range (1000,2,-1):
    c=i
    for m in range(1000-c,1,-1):
        b=m
        a=1000-b-c
        if a**2+b**2==c**2 and a+b+c==1000 and b<c:
          print(f"a = {a}  b = {b}  c ={c}")
          break 
        