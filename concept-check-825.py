class Student:
  idt: int
  major: str
  year: int
  
  def __init__(self, new_id: int) -> None:
    """
    Requires: new_id >= 0
    """
    self.idt = new_id
    self.major = "undeclared"
    self.year = 1
    pass
  