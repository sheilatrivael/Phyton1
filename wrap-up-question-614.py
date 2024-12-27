import check
def mult_table(n: int) -> list[list[int]]:
    '''
    Returns the n+1 by n+1 multiplication table
    
    Requires: n >= 0
    
    Examples: 
       mult_table(0) => [[0]]
       mult_table(1) => [[0, 0], 
                         [0, 1]]
       mult_table(2) => [[0, 0, 0], 
                         [0, 1, 2],
                         [0, 2, 4]]
       mult_table(5) => [[0, 0, 0, 0, 0, 0], 
                         [0, 1, 2, 3, 4, 5],
                         [0, 2, 4, 6, 8, 10],
                         [0, 3, 6, 9, 12, 15],
                         [0, 4, 8, 12, 16, 20],
                         [0, 5, 10, 15, 20, 25]]
    '''    
    
    #create a multiplication table (n+1)x(n+1)
    if n==0:
      return [[0]]
    else:
      return [ [row*col for col in range(n+1)] for row in range(n+1) ]

    pass
  
check.expect("Test 1", mult_table(0), [[0]])

check.expect("Test 2", mult_table(1), [[0, 0], 
                                      [0, 1]])
                                      
check.expect("Test 3", mult_table(2), [[0, 0, 0], 
                                      [0, 1, 2],
                                      [0, 2, 4]])
                                      
check.expect("Test 4", mult_table(5), [[0, 0, 0, 0, 0, 0], 
                                      [0, 1, 2, 3, 4, 5],
                                      [0, 2, 4, 6, 8, 10],
                                      [0, 3, 6, 9, 12, 15],
                                      [0, 4, 8, 12, 16, 20],
                                      [0, 5, 10, 15, 20, 25]] )
  