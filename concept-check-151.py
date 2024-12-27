import math

def third_side(opp: float, hyp: float) -> float:
  """
  Pythagorean Theorem given the hypotenuse
  in hyp and opposite side in opp

  Requires:
     0.0 < opp < hyp
     
  Examples:
     third_side(4.0, 5.0) => 3.0
  """
  ##YOUR CODE GOES HERE
  y = opp**2
  z = hyp**2
  x = math.sqrt(z-y)
  return x
  pass

#Typical values, small and large values
check.within("Example 1", third_side(4.0, 5.0), 3.0, 0.00001)
check.within("Example 2", third_side(5.0, 13.0), 12.0, 0.00001)
check.within("Example 3", third_side(500000.0, 1300000.0), 1200000.0, 0.00001)

#Boundary values
#Special cases
#Relationship between parameters
