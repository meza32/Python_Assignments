name = "Muhammed"
password = "qwerasdf321!"
name_entered = (input('Please enter your first name : ')).title().strip()
if name_entered == name:
  print('Hello, Muhammed! The password is : qwerasdf321!')
else:
  print(f"Hello, {name_entered}! See you later.")