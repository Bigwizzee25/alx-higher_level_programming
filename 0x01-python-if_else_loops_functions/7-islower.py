#!/usr/bin/python3
def islower(c):
  # Get the ASCII code of the character.
  ascii_code = ord(c)

  # Check if the ASCII code is between 97 and 122.
  # These are the ASCII codes for lowercase characters.
  return 97 <= ascii_code <= 122

print(islower('a'))