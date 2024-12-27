import check
def vowel(word: str) -> int:  #helper function
  
  vowels = "aiueoAIUEO"
  count = 0
  for char in word: #'a' in 'abb'
    if char in vowels: #'a' in vowels
      count += 1
  return count

def vowel_sort(los: list[str]) -> None:
  """
  Mutates the list los so that the elements are sorted in 
  increasing order of the number of vowels (either upper
  or lower case) in the string.
  
  Effects: Mutates los
  
  Examples:
     If L = [] then
     vowel_sort(L) => None
     and L is unchanged
  
     If L = ['aaa', 'adt', 'ab', 'aziubapiqulwerknii', 'eeeeee'] then
     vowel_sort(L) => None
     and L is mutated to ['adt', 'ab', 'aaa', 'eeeeee', 'aziubapiqulwerknii']
     
     If L = ['dog', 'cat', 'fish', 'yyz', 'tuna', 'elephant'] then
     vowel_sort(L) => None
     and L is mutated to ['yyz', 'dog', 'cat', 'fish', 'tuna', 'elephant']
  """
  
  los.sort(key = lambda word: vowel(word)) #word is each element in los 'abb' 
  pass

L = ['abb', 'aab', 'aaa']
check.expect("Ex 1 - empty list", vowel_sort(L), None)
check.expect("Ex 1 Mutation", L, ['abb', 'aab', 'aaa'])

L = []
check.expect("Ex 1 - empty list", vowel_sort(L), None)
check.expect("Ex 1 Mutation", L, [])

L = ['aaa', 'adt', 'ab', 'aziubapiqulwerknii', 'eeeeee']
check.expect("Ex 2", vowel_sort(L), None)
check.expect("Ex 2 Mutation", L, ['adt', 'ab', 'aaa', 'eeeeee', 'aziubapiqulwerknii'])

L = ['dog', 'cat', 'fish', 'yyz', 'tuna', 'elephant']
check.expect("Ex 3", vowel_sort(L), None)
check.expect("Ex 3 Mutation", L, ['yyz', 'dog', 'cat', 'fish', 'tuna', 'elephant'])