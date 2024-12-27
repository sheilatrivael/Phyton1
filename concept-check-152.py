import math

def cosine_law(a: float, b: float, theta: float) -> float:
  """
  Returns the third side length using 
  the cosine law with side lengths a and b 
  and contained angle theta in radians
  
  cosine_law: Float Float Float -> Float
  Requires:
     0.0 < a
     0.0 < b
     0.0 < theta < math.pi
     
  Example:
     cosine_law(3, 4, math.pi/3) => 3.60555127546
  """
  ##YOUR CODE GOES HERE
  c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta))
  return c
  pass

cosine_law(3, 4, 1/2*math.pi)
cosine_law(5, 12, 1/2*math.pi)
cosine_law(9, 10, 47/180*math.pi)
cosine_law(4, 5, 36.87/180*math.pi)
cosine_law(3, 5, 53.13/180*math.pi)