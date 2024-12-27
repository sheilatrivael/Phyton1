from typing import Any

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
    
  def __eq__(self, other: Any) -> bool:
    """
    Returns True if the movies are equal
    and False otherwise
    """
    return isinstance(other, Movie) and\
           self.name == other.name and\
           self.year == other.year and\
           self.rating == other.rating
