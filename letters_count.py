sentence = "hippo runs to us!"
letter = {}
liste =[]

for i in sentence:
  
  if i in liste:
    liste.append(i)
    letter[i] = liste.count(i)

  else:
    liste.append(i)
    letter[i] = liste.count(i)

print(letter)