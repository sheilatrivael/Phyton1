import check
def most_points(filename: str) -> str:
  '''
  Returns player with most points
  give the data in filename
  
  Effects:
     Reads form a file
     
  Requires: 
     Unique player with maximum
     filename exists, is nonempty 
     and is of the correct format
     
  Examples:
     most_points("1985.txt") => 'Wayne Gretzky'
     where "1985.txt" consists of
     Wayne Gretzky,52,163
     Mario Lemieux,45,93
     Paul Coffey,48,90
  '''
  #open and read a file
  fin = open(filename, "r")
  content = fin.readlines() #list of strings ["Wayne Gretzky", "52", "163"]
  M = [line.split(",") for line in content]
  D = {}
  for each in M:
    player = each[0]
    goals = int(each[1])
    assists = int(each[2])
    points = goals + assists
    D[player] = points
  return max(D, key=D.get) #compare the values (points) in D,return the key= player
  
  fin.close()
  
  return lines
  pass

check.expect("Test 1", most_points("1985.txt"), 'Wayne Gretzky')