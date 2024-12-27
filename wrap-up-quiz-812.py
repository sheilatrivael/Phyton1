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
        
        
  def area(self) -> float:
    """
    Returns the area of self based on the units as specified in is_metric.
    
    area: Room -> Float
    
    Example:
       n = Room(1.0, 1.0, True)
       n.area() => 1.0
       
       n = Room(2.0, 3.0, False)
       n.area() => 6.0
    """
  
    ans = self.length*self.width 
    return ans
    pass
  
n = Room(1.0, 1.0, True) #True means in meter, we want area in meter?
check.within("Ex 1", n.area(), 1.0, 0.00001)

n = Room(2.0, 3.0, False) #False mean in feet we want area in feet?
check.within("Ex 2", n.area(), 6.0, 0.00001)
