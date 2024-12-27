import check


##Copied from above
def character_count(sentence: str) -> dict[str, int]:
  """
  Returns a dictionary that consists of a character
  and count of each character in the string sentence.
  
  Examples:
     character_count("") => {}
     character_count("banana") => {'a':3, 'b': 1, 'n':2}
  """
  characters = {}
  for char in sentence:
    characters[char] = characters.get(char, 0) + 1
  return characters
    
## Next, find the most common character in a string
def most_common_character(sentence: str) -> list[str]:
  """
  Returns the most common character in the string sentence.
  If there is a tie, returns the most common characters
  in the order they first appear in sentence.
   
  Requires: 0 < len(sentence)
     
  Examples: 
    most_common_character("c") => ["c"]
    most_common_character("banana") => ["a"]
    most_common_character("xbananaxx") => ["x", "a"]
  """

  ##EDIT THE CODE BELOW
  chars = character_count(sentence)
  most_common = []
  max_times = 0
  for curr_char in chars:  

    if chars[curr_char] == max_times:
      most_common += [curr_char]
      max_times = chars[curr_char] #3
      
    if chars[curr_char] > max_times: # 3 > 0
      most_common = [curr_char] #x
      max_times = chars[curr_char] #3
      
  return most_common

check.expect("Test 3", most_common_character("xbananaxx"), ["x", "a"])
check.expect("Test 2", most_common_character("banana"), ["a"])
check.expect("Test 1", most_common_character("c"), ["c"])
