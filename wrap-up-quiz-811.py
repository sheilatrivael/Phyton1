import check
from typing import Any

class Room:
  length: float
  width: float
  is_metric: bool

  metres_to_feet = 3.28084
  
  def __init__(self, l, w, in_metric):
    """
    Initializes a Room object
    by calling Room(l, w, in_metric).
    
    Effects: Mutates self
    
    __init__: Room Float Float Bool -> None
    Requires: 
       0.0 < l
       0.0 < w
    """
    self.length = l
    self.width = w
    self.is_metric = in_metric
    
  def __eq__(self, other: Any) -> bool:
    """
    Returns True if self and other are considered 
    equal and False otherwise.
    """
    return isinstance(other, Room) and \
      self.is_metric == other.is_metric and \
      abs(self.length-other.length) < 0.00001 and\
      abs(self.width-other.width) < 0.00001
        
  def switch_units(self) -> None:
    """
    Converts to/from metric based on what is_metric is.
    
    Effects: Mutates self
    
    Example:
       n = Room(1.0, 1.0, True)
       n.switch_units() => None
       and n is mutated to Room(3.28084, 3.28084, False)
       
       r = Room(3.28084, 3.28084, False)
       r.switch_units() => None
       and r is mutated to Room(1.0, 1.0, True)
    """
    
    if self.is_metric: #if it's in metric, True, convert to feet
      self.length *= self.metres_to_feet
      self.width *= self.metres_to_feet
      self.is_metric = False #it's in feet now
    else: #if it's in feet, False, convert to metric
      self.length /= self.metres_to_feet
      self.width /= self.metres_to_feet
      self.is_metric = True #it's in metric now
    
    pass
  
n = Room(1.0, 1.0, True) #in meter
check.expect("Ex 1", n.switch_units(), None)
check.expect("Ex 1 Mutation", n, Room(3.28084, 3.28084, False)) #in feet

r = Room(3.28084, 3.28084, False) #in feet
check.expect("Ex 2", n.switch_units(), None)
check.expect("Ex 2 Mutation", n, Room(1.0, 1.0, True)) #in metric