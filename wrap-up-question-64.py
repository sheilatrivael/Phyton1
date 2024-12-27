from typing import Any, TypeVar
X = TypeVar('X') 

import check
def key(d: dict[X, Any], v: Any) -> X|None:
  '''
  Returns the key k corresponding to d[k] == v
  or None if no such key exists
  
  Requires: 
     At most one key k satisfying d[k] == v
  
  Examples:
     key({0: 'zero', 1: 'one'}, 'one') => 1
     key({0: 'zero', 1: 'one'}, 'two') => None
  '''
  

  for key, value in d.items():
    if value == v:
      return key
  else:
    return None
  pass

check.expect("Test 1", key({0: 'zero', 1: 'one'}, 'one'), 1)
check.expect("Test 2", key({0: 'zero', 1: 'one'}, 'two'), None)
