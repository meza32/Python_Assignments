def leap_year(year):
  return (lambda x :print(f"{x} is a leap year") if x % 100 != 0 and x % 4 ==0 or x % 400 ==0   else print(f"{x} is not a leap year"))(year)
leap_year(1800)