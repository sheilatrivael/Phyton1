import check
def column(grid: "Grid", col_num: int) -> list[int]:
  '''
  Returns the col_num column of grid
  
  Requires: 
     grid is not empty
     0 <= col_num <= len(grid)-1
  
  Examples:
     column([[1]], 0) => [1]
     column([[10,2],[20,1]], 1) => [2, 1]
  '''
  
  ans = []
  for row in range(len(grid)):
    for c in range(len(grid)):
      if c == col_num:
        ans += [grid[row][col_num]]
  return ans
  

check.expect("Ex 1", column([[1]], 0), [1])
check.expect("Ex 2", column([[10,2],[20,1]], 1), [2, 1])
check.expect("Ex 3", column([[10,2],[20,1]], 0), [10, 20])
check.expect("Ex 3", column([[1,2,3],[4,5,6],[7,8,9]], 0), [1, 4, 7])