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
    ##YOUR CODE FROM ABOVE GOES HERE IF DESIRED FOR TESTING
    pass
        
def str_name(s: str) -> Name:
    """
    Returns Name from s, where s has the form 
    "first last" or "first last\n"
    but s may include extra whitespaces
    
    Example:
       str_name("Carmen Bruni\n") => Name("Carmen", "Bruni")
    """
  
    s = s.strip().split() #this will return a list of string ["Carmen", "Bruni"]
    return Name(s[0], s[1])
    pass
  
check.expect("T1", str_name("Carmen Bruni"), Name("Carmen", "Bruni"))
check.expect("T2", str_name("Carmen Bruni\n"), Name("Carmen", "Bruni"))