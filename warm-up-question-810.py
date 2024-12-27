import check
def total(t: tuple[int], fnameout: str) -> None:
  """
  Writes the sum of t in fnameout.
  
  Effects:
     Writes to a file
  
  Examples:
     total((),"empty.txt") => None
     and empty.txt contains:
     0
     
     total((1,2,3),"ex1.txt") => None
     and ex1.txt contains:
     6

  """
   
  #write the file
  fout = open(fnameout, "w")
  
  fout.write(str(sum(t)) + "\n")
  
  fout.close()
  pass

check.set_file_exact("empty.txt", "expected2.txt")
check.expect("Test 2", total((),"empty.txt"), None)

check.set_file_exact("ex1.txt", "expected1.txt")
check.expect("Test 1", total((1,2,3),"ex1.txt"), None)