import check
def climate_action_initiative(n: int, init: int) -> float:
  """
  Returns the amount on a tax return for the Carbon Tax Rebate
  
  Requires: 0 < n, init
  
  Examples:
     climate_action_initiative(1, 152) => 152.0
     climate_action_initiative(2, 152) => 228.0
     climate_action_initiative(3, 152) => 266.0
     climate_action_initiative(4, 152) => 304.0
     climate_action_initiative(10, 152) => 304.0
  """
  if n == 1:
    return float(init)
  elif n == 2:
    return float(init*1.5)
  elif n == 3:
    return float(init*1.75)
  else: 
    return float(init*2)
  pass

EPSILON = 0.0001
check.within ("Test 1", climate_action_initiative(1, 152), 152.0, EPSILON)
check.within ("Test 2", climate_action_initiative(2, 152), 228.0, EPSILON)
check.within ("Test 3", climate_action_initiative(3, 152), 266.0, EPSILON)
check.within ("Test 4", climate_action_initiative(4, 152), 304.0, EPSILON)
check.within ("Test 10", climate_action_initiative(10, 152), 304.0, EPSILON)