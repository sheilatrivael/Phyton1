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
    
def longer_title(m1: Movie, m2: Movie) -> str:
  """
  Returns the longer titled movie name of m1 and m2 or 
  the name of m1 if tied.
  
  Example:
     m1 = Movie("Shrek", 2001, 8)
     m2 = Movie("Shrek 2", 2004, 7)
     m3 = Movie("Shrek the Third", 2007, 6)
     longer_title(m1, m2) => "Shrek 2"
     longer_title(m1, m3) => "Shrek the Third"
  """
  
  if len(m1.name) >= len(m2.name):
    return m1.name
  else:
    return m2.name
  pass

m1 = Movie("Shrek", 2001, 8)
m2 = Movie("Shrek 2", 2004, 7)
m3 = Movie("Shrek the Third", 2007, 6)
check.expect("T1", longer_title(m1, m2), "Shrek 2")
check.expect("T2", longer_title(m1, m3), "Shrek the Third")