import check
def name_lengths(filename_in: str, filename_out: str) -> str:
  '''
  Consumes a string filename_in that is a file
  present in the current directory with names first last
  in white space separated format (one name per line)
  and write the lengths of each person's name to 
  a file with the name filename_out.
  
  Effects:
     Reads from file in filename_in
     Writes to file in filename_out
  
  Requires: filename_in is a valid filename in the directory.
  
  Example:
     name_lengths("names-small.txt", "out.txt") => None
     Assuming names-small.txt contains
     John Smith
     Jane Doe
     Mike Lower
     
     then out.txt contains:
     9
     7
     9
     
  '''
  #open file
  fin = open(filename_in, 'r')
  
  #read through file, strip to remove new lines, replace to remove space between
  names = fin.readlines() #returns a list of strings
  length = [len(name.strip().replace(" ","")) for name in names]
  
  fin.close()

  #Write to file
  fout = open(filename_out,"w")
  
  #converts each integer in the list length to a string
  #joins all strings with newline
  for n in length: 
    fout.write(f"{n}\n") #f-strings method
  fout.close()
  pass

check.expect("Test", name_lengths("names-small.txt", "out.txt"), None)