# Green Glass Door (7 kyu)

# https://www.codewars.com/kata/5642bf07a586135a6f000004

# Sprache: Python
# Datum: 2025-10-15

#Task: Step through my green glass door.
#You are given a series of words, and some “pass through” while others do not.
#The rule is: a word can pass through if it contains at least one pair of identical letters next to each other.

#What I learned:
#I learned how to check if a string contains two identical characters
# in a row and how to implement this in a program.
def step_through_with(s):
  index = 0
  for x in range(len(s)-1):
    if s[index]==s[index+1]:
      return True
    index+=1
  return False