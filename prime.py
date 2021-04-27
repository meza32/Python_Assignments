number = int(input("Enter the number: "))
count = 2
while number > count:
    if number % count == 0:
        print(f"{number} is not a prime number.")
        break
    else:
        count += 1
if count == number:
  print(f"{number} is a prime number.")

    