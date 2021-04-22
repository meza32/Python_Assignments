print("Answer the questions with 'Yes' or 'No' only.")
age = input("Are you a cigarette addict older 75 years old? :").title().strip()
chronic =  input("Do you have a severe chronic disease? :").title().strip()
immune = input ("Is your immune system too weak? :").title().strip()

if age=='No' and chronic=='No' and immune == 'No':
    print('You are not in a risky group!')
else:
    print("You are in a risky group!")
