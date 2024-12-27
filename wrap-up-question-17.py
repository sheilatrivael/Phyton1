import math
def n_sphere_volume(n: int, r: float) -> float:
  """
  Returns the volume of the n-sphere of radius r
  
  Requires: 
     2 <= n
     0.0 <= r
  
  Examples:
     n_sphere_volume(2, 1.0) => 3.141592653589793
     n_sphere_volume(3, 1.0) => 4.1887902047863905
  """
  ##YOUR CODE GOES HERE
  numerator = (math.pi**(n/2))*(r**n)
  denominator = math.gamma(n/2 + 1)
  volume = numerator / denominator
  return volume
  pass

n_sphere_volume(2, 1.0)
n_sphere_volume(3, 1.0)