import check
def add_one(filename: str) -> None:
  """
  Returns None but opens filename and
  increments all values by 1 before saving 
  to a file "shifted.txt"
  
  Effects:
     Reads from file
     Writes to a file
  
  Requires:
  	 filename exists
  
  Examples:
     add_one("empty.txt") => None
     and if "empty.txt" is an empty file,
     "shifted.txt" is also empty.
     
     add_one("onetwothree.txt") => None
     and if "onetwothree.txt" contains:
     1
     2
     3
     "shifted.txt" contains
     2
     3
     4
     
     (Notice the extra newline character after the 4).
  """
  
  #open the file
  fin = open(filename, "r")
  content = fin.readlines() #list of strings ["1", "2", "3"]
  fin.close()

  #write the file
  fout = open("shifted.txt", "w")
  
  for line in content:
    fout.write( str(int(line) + 1) + "\n")
  fout.close()
  pass

  
check.set_file_exact("shifted.txt", "expected.txt")
check.expect("Test 1", add_one("onetwothree.txt"), None)

check.set_file_exact("shifted.txt", "expected.txt")
check.expect("Test 2", add_one("empty.txt") , None)