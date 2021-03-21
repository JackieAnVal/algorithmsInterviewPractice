def firstNotRepeatingCharacter(s):
  visited=[]
  for i in range(0, len(s)):
    if s[i] not in visited: 
      if s.count(s[i])==1:
        return s[i]
      visited.append(s[i])
  return "_"



s = input("Please write the word: ")
print(firstNotRepeatingCharacter(s))
#abacabad c
#abacabaabacaba _