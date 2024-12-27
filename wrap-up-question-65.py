import check
def most_ending_digit(L: list[int]) -> int:
  '''
  Returns the single digit that occurs most frequently
  as the last digit of numbers in L. Returns the 
  smallest in the case of a tie.
  
  Requires: 
     len(L) > 0
     L[i] >= 0 for all indices i
  
  Examples:
     most_ending_digit([1,2,3]) => 1
     most_ending_digit([105, 201, 333, 
                        995, 9, 87, 10]) => 5
  '''
  
  M = [i % 10 for i in L] #create a list of all last digits only
  
  #d[k] = v which assigns the value v (frequency) to the key k (the digit)
  d = {}
  for digit in M:
    if digit in d:
      d[digit] += 1
    else: 
      d[digit] = 1
  
  #return the digit with the highest value
  #D[value] allows comparing the values, instead of key themselves
  #if value 5 and 2 both have frequency of 2, it's a tie
  #applying -value makes -5 vs -2 making sure the bigger/max win, which is -2

  return max(d, key = lambda value: (d[value], -value))
  
  pass

check.expect("Test 3", most_ending_digit([1, 5, 5, 2, 3, 2]), 2) #not 5
check.expect("Test 2", most_ending_digit([105, 201, 333, 995, 9, 87, 10]), 5)
check.expect("Test 1", most_ending_digit([1,2,3]), 1)

"""
Tuple creation (d[k], -k)
Now, we apply the lambda function lambda k: (d[k], -k) for each key k:

For k = 1: (d[1], -1) → (1, -1)
For k = 5: (d[5], -5) → (2, -5)
For k = 2: (d[2], -2) → (2, -2) this is the winner since -2 > -5 
For k = 3: (d[3], -3) → (1, -3)
"""