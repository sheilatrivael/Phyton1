import check
def tuple_sort(L: list[tuple[int, int, int]]) \
                -> list[tuple[int, int, int]]:
  """
  Returns a new list of triples sorted by largest median value
  with ties broken by largest product.
  
  Examples:
     tuple_sort([]) => []
     tuple_sort([(1,2,3)]) => [(1,2,3)]
     tuple_sort([(1,2,3), (6,2,5)]) => [(6,2,5), (1,2,3)]
  """
  #create a list(the tuple, the median of sorted t, the product, original index)
  #M = [((1,4,5), 4, 20, 0), ((1,4,6), 4, 24, 1), ((2,4,3), 4, 24, 2)]
  #i will be the original index 0,1,2,3... t will be each tuple in L
  M = [ (t, sorted(t)[1], (t[0]*t[1]*t[2]) , i) for i, t in enumerate(L) ]
  
  
  #sort the list: sorted(iterable, *, key= lambda x:, reverse=True) 
  #reverse=True: high to low, reverse=False is default descending
  # x = ((1,4,5), 4, 20, 0)
  #1. largest median -> x[1] = 4 
  #2. largest product if median same -> x[2] = 20
  #3. original order if median and product same
  sorted_M = sorted(M, key=lambda x: (x[1], x[2]), reverse=True)
  
  #M = [((1,4,6), 4, 24), ((2,4,3), 4, 24), ((1,4,5), 4, 20)]
  #now return all the tuple from the sorted_M = (1,4,6)
  #i = ((1,4,6), 4, 24)
  #i[0] = (1,4,6)
  return list(i[0] for i in sorted_M)
  pass

check.expect("Test 3", tuple_sort( [(1,2,3), (6,2,5)]), [(6,2,5), (1,2,3)])
check.expect("Test equal", tuple_sort([(1, 2, 3), (2, 1, 3), (3, 2, 1)]), [(1, 2, 3), (2, 1, 3), (3, 2, 1)])
check.expect("Test 1", tuple_sort([]), [])
check.expect("Test 2", tuple_sort([(1,2,3)]), [(1,2,3)])

"""
reverse=True sort M in descending order (high to low) by median x[1] first, 
if median the same, it will sort by product x[2],
when both median and product are the same, the origian order is naturally
preserved because phyton's sort is stable. It will keeps elements in their
original relative order when sorting criteria are equal.
"""
