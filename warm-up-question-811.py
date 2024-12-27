import check
def most_recent_championship(fnamein: str) -> dict[str, int]:
  """
  Reads a file fnamein of comma separated team name and year pairs.
  Returns a dictionary of pairs corresponding to the team name and 
  the year they most recently won a championship.
  
  Effects:
     Reads from a file
     Prints to the screen
  
  Requires:
    Each line is of the form:
    comma-less team name,positive integer
  
  Examples:
     most_recent_championship("empty.txt") => {}
     Assuming empty.txt is an empty file.
    
     most_recent_championship("ex1.txt") => {"A": 2022, "B": 1979}
     Assuming ex1.txt contains:
     A,1999
     B,1979
     B,1960
     A,2022
     
     most_recent_championship("doesnt_exist.txt") => {}
     Assuming doesnt_exist.txt does not exist and the
     following is printed to the screen:
     Error reading file

  """
  
  #open and read a file
  
  
  try:
    with open(fnamein, "r") as fin:
      content = fin.readlines() #list of strings ["A", "1999"]
      M = [line.split(",") for line in content]
      
      ans = {}
      for key, value in M:
        value = int(value.rstrip("\n")) #value has newlines, remove first
        if (key not in ans) or (value > ans[key]):
          ans[key] = value
      
      return ans #compare the values (points) in D,return that pair
      print(ans)
      
  except Exception:
    print("Error reading file")
    return {}


  pass


check.expect("Test 1", most_recent_championship("ex1.txt"), {"A": 2022, "B": 1979})

check.expect("Test 2", most_recent_championship("empty.txt"), {})