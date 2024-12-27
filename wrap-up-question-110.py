import math
def normal_distribution(x: float, mean: float, std_dev: float):
  """
  Returns corresponding value of the probability density
  function associated with the normal distribution with mean 
  mean, standard deviation std_dev at the value x.
  
  Requires:
     0 < x, mean, std_dev
     
  Examples:
     normal_distribution(3.0, 5.0, 2.0) => 0.12098536225957168
  """
  
  first = 1 / (math.sqrt(2*(std_dev**2)*math.pi))
  exponent = ((x-mean)**2)/(2*(std_dev**2))
  pdf = first * math.e**(-exponent)
  return pdf
  pass

normal_distribution(3.0, 5.0, 2.0)