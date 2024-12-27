import check
import math

def largest_even_number(a: int, b: int, c: int) -> int:
  """
  Returns the largest even number of a, b or c
  or the smallest number if all are odd
  
  Examples:
     largest_even_number(2, 100, 4) => 100
     largest_even_number(2, 101, 41) => 2
     largest_even_number(-51, 101, 41) => -51
  """
  
  smallest = min(a, b, c)
  largest = max(a, b, c)
  median = (a + b + c) - (largest + smallest)
  print (smallest, median, largest)
    
  if largest % 2 == 0:
    return largest
  if median % 2 == 0:
    return median
  if smallest % 2 == 0:
    return smallest
  else:
    return smallest
  pass


#only one is odd
check.expect ("a is odd", largest_even_number(3, 100, 40), 100) #good
check.expect ("b is odd", largest_even_number(2, 101, 40), 40) #good
check.expect ("c is odd", largest_even_number(2, 100, 41), 100)

#only one is even
check.expect ("a is even", largest_even_number(2, 101, 41), 2)
check.expect ("b is even", largest_even_number(3, 100, 41), 100)
check.expect ("c is even", largest_even_number(3, 101, 40), 40) #good

#two are even
check.expect ("ab are even", largest_even_number(2, 101, 40), 40) #good
check.expect ("bc are even", largest_even_number(3, 100, 40), 100) #good
check.expect ("ac is even", largest_even_number(2, 101, 40), 40) #good

#all even or all odd 
check.expect ("All even", largest_even_number(2, 100, 4), 100) #good
check.expect ("All odd, negative", largest_even_number(-51, 101, 41), -51)

"""
version 1
if (a % 2 == 0):
    print (a,b,c)
    if (b % 2 == 0):
      print (a,b,c)
      if (c % 2 == 0):
        print (a,b,c)
        return max (a,b,c) #if a,b,c are even
      else:
        print (a,b)
        return max (a,b) #if a and b are even, c is odd
    else:
      print (a,c) #a is even, b is odd, c is?
      if (c % 2 == 0):
        return max (a,c) #if a and c are even, b is odd
      else:
        return a #only a is even
  else:
    print(b,c)
    if (b % 2 == 0):
      print (b,c)
      if (c % 2 == 0):
        return max (b,c) #if b and c are even, a is odd
      else:
        return b #only b is even
    else:
      print (a,b,c) #if a is odd, b is odd, c is?
      if (c % 2 == 0):
        return c #only b is even
      else:
        return min(a,b,c) #if all is odd
  pass

version 2
  even_max = None 
  
  if a % 2 == 0:
    even_max = a
  if b % 2 == 0:
    if (even_max == None) or (b > even_max):
      even_max = b
  if c % 2 == 0:
    if (even_max == None) or (c > even_max):
      even_max = c
      return c
    else:
      return b
      
  if even_max == None:
    return min(a,b,c)
  
  return even_max
  pass
  
version 3 from chatgpt
  # Create a list of the numbers
  numbers = [a, b, c]
    
  # Find even numbers
  even_numbers = [num for num in numbers if num % 2 == 0]
    
  if even_numbers:  # If there are even numbers
    return max(even_numbers)  # Return the largest even number
  else:
    return min(numbers)  # If no even numbers, return the minimum
  pass 
"""""