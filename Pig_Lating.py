def Title(string):
  Lower = string.lower()
  Upper = str(string[0])
  Upper_Letter = Upper.upper()
  To_Title = Upper_Letter + Lower[1:]
  return To_Title

Enter = input("Please enter a word: ")
Vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
if Enter[0] in Vowel:
  Upper_String = str(Enter[0])
  Upper = Upper_String.upper()
  New_Word = Upper + Enter[1:] + "way"
  print(New_Word)
else:
  length = len(Enter)
  First_Letter = Enter[0]
  Whole_Word = Enter[2:] + First_Letter + "ay"
  New = Whole_Word.lower()
  Second_Letter = str(Enter[1])
  Second_letter = Second_Letter.upper()
  New_Word = Second_letter + New
  print(New_Word)

print("Title Case: ", Title(Enter))
