# Converts an input string in English text to braille
def braille(s):
  # To adjust decimal when lowercase/uppercase letter converted to integer
  asciiOffsetLower = 97
  asciiOffsetUpper = 65

  # Each element of array represents letter of alphabet in Braille
  alphabet = [[[1,0,0],[0,0,0]], [[1,1,0],[0,0,0]], [[1,0,0],[1,0,0]], [[1,0,0],[1,1,0]],
  [[1,0,0],[0,1,0]], [[1,1,0],[1,0,0]], [[1,1,0],[1,1,0]], [[1,1,0],[0,1,0]], [[0,1,0],[1,0,0]],
  [[0,1,0],[1,1,0]], [[1,0,1],[0,0,0]], [[1,1,1],[0,0,0]], [[1,0,1],[1,0,0]], [[1,0,1],[1,1,0]],
  [[1,0,1],[0,1,0]], [[1,1,1],[1,0,0]], [[1,1,1],[1,1,0]], [[1,1,1],[0,1,0]], [[0,1,1],[1,0,0]],
  [[0,1,1],[1,1,0]], [[1,0,1],[0,0,1]], [[1,1,1],[0,0,1]], [[0,1,0],[1,1,1]], [[1,0,1],[1,0,1]],
  [[1,0,1],[1,1,1]], [[1,0,1],[0,1,1]]]

  # Represent space character in Braille
  space = [[0,0,0],[0,0,0]]
  # Braille capitalization mark
  capital = [[0,0,0],[0,0,1]]

  # Stores arrays in each which represent letter in Braille
  brailleArray = []
  # Stores final string of Braille characters
  braille = ""
  
  # Iterating over input string
  for i in range(0, len(s)):
      currChar = s[i]
      # If character is space
      if(currChar.isspace()):
        brailleArray.append(space)
      # If character is lowercase letter
      elif(currChar.islower()):
        # Converts char to decimal and offsets to find position in alphabet array
        asciiPos = ord(currChar)
        alphabetPos = asciiPos - asciiOffsetLower
        lowerLetter = alphabet[alphabetPos]
        brailleArray.append(lowerLetter)
      # If character is uppercase letter
      elif(currChar.isupper()):
        # Converts char to decimal and offsets to find position in alphabet array
        asciiPos = ord(currChar)
        alphabetPos = asciiPos - asciiOffsetUpper
        upperLetter = alphabet[alphabetPos]
        # Braille capitalization mark added before letter
        brailleArray.append(capital)
        brailleArray.append(upperLetter)
  
  # Adds each element of Braille array to string in order
  for letter in brailleArray:
    for half in letter:
      for element in half:
        braille += str(element)
    braille += " "
  
  return braille

test = input("Please enter a string: ")
print("\nInput String: \n"+test)
print("\nBraille: \n"+braille(test))