import check
def userid(first_name: str, middle_name: str, last_name: str) -> str:
  """
  Returns the at most 8 character user id 
  given the first middle and last name
  
  Requires:
     1 <= len(first_name)
     1 <= len(last_name)
     
  Examples:
     userid("Harry", "James", "Potter") => "hjpotter"
     userid("Ronald", "Bilius", "Weasley") => "rbweasle"
     
  """
  first = first_name[:1] 
  middle = middle_name[:1] 
  last = last_name
  fml = first + middle + last
  user = fml.lower()
  return user[0:8]
  pass

#Test
check.expect("Test1", userid("Harry", "James", "Potter"), "hjpotter")
check.expect("Test2", userid("Ronald", "Bilius", "Weasley"), "rbweasle")
check.expect("Test3", userid("Albus", "", "Dumbledore"), "adumbled")
