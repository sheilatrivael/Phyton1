import check
def name_change(old, new_last):
  """
  Changes the old string's last name to the string new_last
  
  name_change: Str Str -> Str
  Requires:
     old contains at least one space separating first
     and last name.
  
  Examples:
     name_change("John Doe", "Smith") => "John Smith"
     name_change("Bruce Thomas Wayne", "Willis") => "Bruce Thomas Willis"
  """
  last_space = old.rfind(" ")
  return old[:last_space] + " " + new_last
  pass

check.expect("Test0", name_change("King A B C Doe", "Smith"), "King A B C Smith")
check.expect("Test1", name_change("John A B Doe", "Smith"), "John A B Smith")
check.expect("Test2", name_change("Bruce Thomas Wayne", "Willis"), "Bruce Thomas Willis")
check.expect("Test3", name_change("Tricia Halim", "Susetyo"), "Tricia Susetyo")
check.expect("Test4", name_change("Evelyn Leonardi", "Linardi"), "Evelyn Linardi")