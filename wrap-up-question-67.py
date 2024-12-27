import check
def add_a(L: list[str]):
  '''
  Returns a new list consisting of all strings in L that begin with 
  the letter a.  Elements should be returned respecting their 
  relative order in L.
  
  Examples:
     add_a([]) => []
     add_a(["apricot", "apple", "banana", "avocado"]) 
       =>  ["apricot", "apple", "avocado"])
  '''
  
  return [word for word in L if word[0:1] == 'a']

  pass


check.expect("Test 2", add_a(["apricot", "apple", "banana", "avocado"]), \
                  ["apricot", "apple", "avocado"])
check.expect("Test 1", add_a([]), [])
