import check
def record_digits(s: str) -> tuple[int, int, int, int, int,
                                   int, int, int, int, int]:
  '''
  Returns a list of 10 numbers corresponding to the 
  number of occurrences of each digit in the string s
  
  Examples:
     record_digits("") => (0, 0, 0, 0, 0, 
                           0, 0, 0, 0, 0)
     record_digits("banana") => (0, 0, 0, 0, 0, 
                                 0, 0, 0, 0, 0)
     record_digits("34298465fsdf3") => (0, 0, 1, 2, 2, 
                                        1, 1, 0, 1, 1)
  '''
  
  #create a list of digits only, can use filter too
  L = [i for i in s if i.isdigit()] 
  L.sort()
  
  #create a dictionary from '0' to '9' (key), set all counts to 0 (value)
  d = {str(i) :  0 for i in range(10)}

  #update the dictionary with the counts (value) of each digit
  list(map(lambda digit: d.update({digit: d.get(digit,0) + 1}) ,L))

  #return a tuple with all the values = d[i] from the dictionary, str(i) is key
  return tuple(d[str(i)] for i in range(10))
  pass

check.expect("Test 3", record_digits("34298465fsdf3"), (0, 0, 1, 2, 2, 1, 1, 0, 1, 1))
check.expect("Test 1", record_digits(""), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
check.expect("Test 2", record_digits("banana"), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


"""
Syntax: d.update({key: value}) --> key=digit, value=count=d.get(digit,0) + 1
If the key is already in the dictionary, it updates the value associated with that key.
If the key is not in the dictionary, it adds a new key-value pair.

characters[char] = characters.get(char, 0) + 1 from module 6.2
"""
"""
  # Step 1: Filter digits from the string
  L = list(filter(str.isdigit, s))
  
  # Step 2: Create a dictionary that will store the counts of each digit
  # Initialize the dictionary with all digit counts set to 0
  digit_counts = {str(i): 0 for i in range(10)}
  
  # Step 3: Use map to update the counts in the dictionary
  # We update the count for each digit
  list(map(lambda digit: digit_counts.update({digit: digit_counts.get(digit, 0) + 1}), L))
  
  # Step 4: Convert the dictionary values to a tuple and return
  return tuple(digit_counts[str(i)] for i in range(10))
"""