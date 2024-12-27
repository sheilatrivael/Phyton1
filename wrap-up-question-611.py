from typing import Any, TypeVar
X = TypeVar('X') #Declare an arbitrary but same type below

import check
def common_keys(d1: dict[X, Any], d2: dict[X, Any]) -> list[X]:
  """
  Consumes two dictionaries with the same key type and returns
  a list of all keys occuring in both dictionaries
  
  Examples:
     common_keys({}, {}) => []
     common_keys({}, {0:'zero', 1:'one'}) => []
     common_keys({0:'naught', 2:'deuce', 3: 'trey'},
                 {0:'zero', 1:'one'}) => [0]
  """
  D1 = set(d1.keys())
  D2 = set(d2.keys())
  common = list(D1.intersection(D2))
  return common
  
  
  pass

check.expect("Test 3", common_keys({0:'naught', 2:'deuce', 3: 'trey'}, \
                 {0:'zero', 1:'one'}), [0])
check.expect("Test 1", common_keys({}, {}), [])
check.expect("Test 2", common_keys({}, {0:'zero', 1:'one'}), [])
