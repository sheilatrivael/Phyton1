import check

class Movie:
  name: str
  year: int
  rating: int

  def __init__(self, n: str, y: int, r: int) -> None:
    """
    Constructor: Create a Movie object by 
    calling Movie(n, y, r)
      
    Effects: Mutates Self
    Requires:
      y > 0
      0 <= r <= 10
    """
    self.name = n
    self.year = y
    self.rating = r
    
def best_movie(lom: list[Movie]) -> Movie:
  """
  Returns the best Movie in lom.
  
  Requires: len(lom) > 0
  
  Example:
     m = Movie("Shrek", 2001, 8)
     m2 = Movie("Shrek 2", 2004, 7)
     m3 = Movie("Shrek the Third", 2007, 6)
     best_movie([m, m2, m3]) => m
  """
  
  ans = lom[0] #"Shrek"
  for title in lom: 
    if title.rating > ans.rating: #"Shrek 2" rating 7 > "Shrek" rating 8 False
      ans = title
  return ans #returns m 
  
  pass

m = Movie("Shrek", 2001, 8)
m2 = Movie("Shrek 2", 2004, 7)
m3 = Movie("Shrek the Third", 2007, 6)
check.expect("T1", best_movie([m, m2, m3]), m)