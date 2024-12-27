import check
def count_char(fnamein: str, char: str) -> int|None:
  """
  Returns the total number of times char occurs in
  the file specified by fnamein. An error message
  is printed if the read fails and None is returned.
  
  Effects: 
    Reads from a file
    Prints to screen
  
  Requires: len(char) == 1
  
  Examples:
    count_char("empty.txt", "a") => 0
    Assuming "empty.txt" exists and is an empty file
    
    count_char("does_not_exist.txt", "a") => None
    Assuming "does_not_exist.txt" doesn't exists 
    and the following is printed:
    File cannot be read
    
    count_char("fruit.txt", "a") => 5
    Assuming "fruit.txt" exists and contains
    apple
    banana
    cherry
    durian
    
  """
  try:
    with open(fnamein, 'r') as fin:
      all_strings = fin.readlines()
      ans = 0
      for string in all_strings:
        ans += string.count(char)
      return ans
      print(ans)
  except Exception:
    print("File cannot be read")
    return None
    
  pass

check.expect("Test 3", count_char("empty.txt", "a"), 0)
check.expect("Test 1", count_char("fruit.txt", "a"), 5)

check.expect("Test 2", count_char("does_not_exist.txt", "a"), None)

