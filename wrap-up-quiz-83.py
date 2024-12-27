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
  
  def __repr__(self) -> str:
    """
    Returns a representation of the Movie object
    """
  
    s = "{0.name} ({0.year}), {0.rating}"
    return s.format(self)
    pass