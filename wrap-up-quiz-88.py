import check
class Movie:
  name: str
  year: int
  rating: int

  def __init__(self, n: str, y: int, r: int) -> None:
    """
    Constructor: Create a Movie object by 
    calling Movie(n, y, r)
      
    Effects: Mutates Self
    Requires:
      y > 0
      0 <= r <= 10
    """
    self.name = n
    self.year = y
    self.rating = r
    
def movie_sort(lom: list[Movie]) -> None:
  '''
  Returns None and mutates lom to sorted order
  by name field excepting "The" words.
  
  Effects: Mutates lom
  
  Example:
     m = Movie("Shrek", 2001, 8)
     n = Movie("The Lord of the Rings: The Fellowship of the Ring",
              2001, 9)
     L = [m, n]
     movie_sort(L) => None
     and L is mutated to [n, m]
  '''
  
  #helper function
  def remove_the (word : Movie) -> str:
    
    a = word.name.lower() #make it all low first
    if a.startswith("the "):
      return a[4:]
    else:
      return a
  
  #after "the" is removed, then sort
  lom.sort(key = remove_the)
  pass


# Test cases
m = Movie("Shrek", 2001, 8)
n = Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, 9)

L = [m, n]

# Test: Sorting should return None
check.expect("Ex 1", movie_sort(L), None)

# Test: L should now be sorted in order
check.expect("Ex 1 Mutation", L, [n, m])