import check
from typing import Any

class Name:
  first: str
  last: str
  
  def __init__(self, fn: str, ln: str) -> None:
    """
    Initializes a Name object
    by calling Name(fn ln).
    
    Effects: Mutates self
    """
    self.first = fn
    self.last = ln
        
  def __eq__(self, other: Any) -> bool:
    """
    Returns True if self and other are 
        considered equal, and False otherwise
    """
    return isinstance(other, Name) and \
      self.first == other.first and \
      self.last == other.last
    
        
  def __repr__(self) -> str:
    """
    Returns a representation of the form:
    "self.last, self.first"
      
    Example:
       n = Name("Carmen", "Bruni")
       str(n) => "Bruni, Carmen"
    """
    
    s = "{0.last}, {0.first}"
    return s.format(self)
    pass
  
carmen = Name("Carmen", "Bruni")
sheila = Name("Sheila", "Trivael")
print(carmen)
print(sheila)