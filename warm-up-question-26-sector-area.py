import math
def sector_area(r: float , theta: float): -> float:
  '''
  Returns the area of a sector of a circle
  given the radius r and angle theta
  
  sector_area: Float Float  -> Float
  Requires:
     0.0 <= r
     0.0 <= theta <= 2*math.pi
     
  Example:
     sector_area(0.0, 0.0) => 0.0
     sector_area(1.0, math.pi/2) => 0.785398163397
  '''
  ##YOUR CODE GOES HERE
  A = 1/2 * (r**2) * theta
  return A
  pass

sector_area(7, 5/7*math.pi)