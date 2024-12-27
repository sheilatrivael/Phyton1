def is_leap_year(n: int) -> bool:
  """
  Returns True if n is a leap year and False otherwise.
  
  Requires: 0 < n
  
  Examples:
     is_leap_year(1) => False
     is_leap_year(4) => True
     is_leap_year(100) => False
     is_leap_year(400) => True
     
  note to self:(n % 400 == 0) or (n % 4 == 0 and n % 100 != 0) 
  """
  
  if n % 4 == 0:
    if n % 100 == 0:
      if n % 400 == 0:
        return True # if n is divisible by 4, 100, and 400
      else:
        return False # if n is divisible by 4, 100 but not 400
    else:
      return True
  else: 
    return False
    
  pass

is_leap_year(1) #F
is_leap_year(4) #T
is_leap_year(100) #F
is_leap_year(400) #T
is_leap_year(2028) #T
is_leap_year(2000) #T
is_leap_year(2100) #F
is_leap_year(1800) #F
is_leap_year(2024) #T
is_leap_year(2028) #T