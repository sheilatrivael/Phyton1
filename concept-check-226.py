def opposite(x: bool, y: bool) -> bool:
  """
  Returns True if x and y have opposite
  truth values and False otherwise.
  
  Example:
     opposite(True, True) => False
  """
  #YOUR CODE GOES HERE
  return x!=y
  pass

opposite(True, True) #False
opposite(True, False) #True
opposite(False, True) #True
opposite(False, False) #False