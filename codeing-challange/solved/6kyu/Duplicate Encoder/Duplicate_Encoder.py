#Duplicate Unicode kyu6

def duplicate_encode(word):
  word = word.lower()
  new_txt =""
  count =1
  mehrmals =[]
  for buchstabe in word:
    if buchstabe in word and buchstabe in word[count:]:
      new_txt+=")"
      mehrmals.append(buchstabe)
    elif buchstabe in mehrmals:
      new_txt+=")"
    else:
      new_txt+="("
    count+=1
  return new_txt