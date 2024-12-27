import check
def length_alphabetic_sort(los: list[str]) -> list[str]: 
  """
  Returns a new list so that the elements of los are sorted 
  in decreasing order of length with ties broken by 
  increasing alphabetic order
  
  Examples:
     length_alphabetic_sort([]) => []
     length_alphabetic_sort(['apple', 'banana', 'anana']) 
        => ['banana', 'anana', 'apple']
  """
  
  #use key = lambda with 2 conditions
  return sorted(los, key = lambda x: (-len(x), x)) #decreasing
  pass

check.expect("Test 1", length_alphabetic_sort([]), [])
check.expect("Test 2", length_alphabetic_sort(['apple', 'banana', 'anana']) , ['banana', 'anana', 'apple'])

"""
Negative numbers are "smaller" than positive numbers. So, a more negative number is considered smaller in value.
When you reverse a list or sort in descending order, the more negative numbers come first in the sorted list.
"""