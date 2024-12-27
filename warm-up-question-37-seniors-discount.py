import check

def seniors(age: int, cost: float) -> float:
  """
  Returns the cost of a meal given the age and cost plus a 2 dollar tip.
  people 55 or over get 15% off.
  
  Requires: 0 <= age
  
  Examples:
     seniors(0, 10.0) => 12.0
     seniors(55, 10.0) => 10.5
  """
  if 0 <= age < 55:
    total = cost + 2
    return total
  elif age >= 55:
    total = (cost - (cost*0.15) + 2)
    return total
  pass

check.within ("Test 1", seniors(0, 10.0), 12.0, 0.0001)
check.within ("Test 2", seniors(25, 20.0), 22.0, 0.0001)
check.within ("Test 3", seniors(55, 10.0), 10.5, 0.0001)
check.within ("Test 3", seniors(70, 20.0), 19, 0.0001)