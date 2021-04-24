number = input('Enter your number : ')
if number.isnumeric():
  number =int(number)
  digit = len(list(str(number)))
  num_list = list(str(number))
  sum = 0
  for i in range(digit):
    sum += int(num_list[i])**digit
  if sum == number:
    print(f'{number} is an Armstrong number!')
  else:
    print(f'{number} is not an Armstrong number!')
else: 
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")