import check
def pig_latin(s: str) -> str:
  """
  Given a lower case Latin alphabet string s, return the 
  Pig Latin equivalent of the word.
  
  Requires:
     s contains only letters from the lower case Latin alphabet.
     s is nonempty.
  
  Examples:
     pig_latin('apple') => 'appleway'
     pig_latin('your') => 'ouryay'
     pig_latin('sun') => 'unsay'
  """
  first = s[0]
  if (first == 'A') or (first == 'I') or (first == 'U') or (first == 'E') \
or (first == 'O') or (first == 'a') or (first == 'i') or (first == 'u') \
or (first == 'e') or (first == 'o'):
    return s + 'way'
  else:
    s = s[1:] 
    return s + first +'ay'
  pass

check.expect("Test1", pig_latin('apple'), 'appleway') 
check.expect("Test2", pig_latin('your'), 'ouryay')
check.expect("Test3", pig_latin('sun'), 'unsay')