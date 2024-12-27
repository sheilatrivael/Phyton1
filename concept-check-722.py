import check
def longest_name(filename: str) -> str:
  '''
  Consumes a string filename that is a file
  present in the current directory with names first last
  in white space separated format (one name per line)
  and returns the person with the longest name 
  (or the first person in the case of a tie)
  
  Effects: 
     Reads from file in filename
  
  Requires: filename is a valid filename in the directory.
  
  Example:
     longest_name("names-small.txt") => 'John Smith'
     Assuming names-small.txt contains
     John Smith
     Jane Doe
     Mike Lower
     
  '''
  fin = open(filename, 'r')
  
  longest = fin.readline().strip()
  ct = len(longest)
  
  for line in fin: #name = 'John Smith'
    name = line.strip()
    current_ct = len(name)
    if current_ct > ct:
      longest = name #if shorter, longest stay as John Smith
 
  return longest
  
  fin.close()
  
  pass

check.expect("Ex 1", longest_name('name.txt'), "John Smith")
