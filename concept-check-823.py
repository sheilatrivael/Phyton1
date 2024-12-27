import check
from typing import Any, Self
   
class Country: 
  continent: str
  leader: str
  population: int
  
  def __init__(self, cont: str, lead: str, pop: int) -> None:
    self.continent = cont
    self.leader = lead
    self.population = pop

  def __repr__(self) -> str:
    s = "CNT: {0.continent}; L: {0.leader}; POP: {0.population}"
    return s.format(self)

  def __eq__(self, other: Any) -> bool:
    return isinstance(other, Country) and \
         self.continent == other.continent and\
         self.leader == other.leader and\
         self.population == other.population

  def higher_population(self, c: Self) -> Self:
    '''
    Returns the country of self and c with
    the higher population (self if tied)
  
    Example:
       canada = Country("North America", "Trudeau", 37742157)
       india = Country("Asia", "Modi", 1380004385)
       canada.higher_population(india) => india
    '''
    ##YOUR CODE GOES HERE
    pass
  
    if self.population >= c.population:
      return self
    else:
      return c
    pass

canada = Country("North America", "Trudeau", 37742157)
india = Country("Asia", "Modi", 1380004385)
check.expect("T1", canada.higher_population(india), india)