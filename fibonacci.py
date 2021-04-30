fibo=[1]
num =1
while num<56:
  fibo.append(num)
  
  num = fibo[-2]+fibo[-1]
  
print(fibo)
