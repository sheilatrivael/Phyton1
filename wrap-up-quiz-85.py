import check
from typing import Self

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
    
  def is_oldest_movie(self, lom: list[Self]) -> bool:
    """
    Returns True if self is older than all movies in lom
    and False otherwise
  
    Examples:
       m = Movie("Shrek", 2001, 8)
       m2 = Movie("Shrek 2", 2004, 7)
       m3 = Movie("Shrek the Third", 2007, 6)
       m.is_oldest_movie([m2, m3]) => True
       m3.is_oldest_movie([]) => True
       m3.is_oldest_movie([m2]) => False
    """
    if not lom:
      return True
    
    #if m 2001 < m2 2004 and m3 2007 --> True m is the oldest movie
    for title in lom:
      if self.year >= title.year:
        return False
        
    return True #if no movie is older than 2001, then self is oldest
    pass
  
m = Movie("Shrek", 2001, 8)
m2 = Movie("Shrek 2", 2004, 7)
m3 = Movie("Shrek the Third", 2007, 6)
check.expect("T1", m.is_oldest_movie([m2, m3]), True) #2001 < 2004 and 2007 True
check.expect("T2", m3.is_oldest_movie([]), True) #2007 < nothing True
check.expect("T3", m3.is_oldest_movie([m2]), False) #2007 < 2004 False