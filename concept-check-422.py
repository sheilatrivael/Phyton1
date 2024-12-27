import check
def remove_all_vowels() -> str:
  """
  Reads input from the keyboard and takes this string and returns
  this string with all upper or lower case vowels removed.
  
  Effects:
     Reads input from keyboard.
  
  Examples:
    remove_all_vowels() => ""
    if the empty string is given by user input
    
    remove_all_vowels() => "bnn"
    if the string "banana" is given by user input
  """
  s = input("Enter a string: ")
  pos = 0
  answer = ""
  vowels = "aiueoAIUEO"
  if s == "":
    return ""
  while pos < len(s):
    if s[pos] not in vowels:
      answer += s[pos]
    pos += 1
  return answer
  pass


#Test
check.set_input("")
check.expect("Test 0", remove_all_vowels(), "")

check.set_input("banana")
check.expect("Test 2", remove_all_vowels(), "bnn")

check.set_input("BAnanA")
check.expect("Test 3", remove_all_vowels(), "Bnn")