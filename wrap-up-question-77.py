import check
def print_every_kth_char(k: int) -> None:
  '''
  Prints every kth character to the screen
  
  Effects:
     Prints to screen
  
  Requires: k > 0
  
  Examples:
     print_every_kth_char(1) => None
     and every character from a to z is printed on its own line
     
     print_every_kth_char(10) => None
     and the following is printed:
     a
     k
     u
  '''
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  ans = ""
  for char in range(0, len(alphabets), k):
    ans += alphabets[char] + "\n"
  print(ans.rstrip()) #delete the extra newlines at the end

  pass

check.set_print_exact("a\nk\nu")
check.expect("Test 1", print_every_kth_char(10), None)

check.set_print_exact("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz")
check.expect("Test 2", print_every_kth_char(1), None)