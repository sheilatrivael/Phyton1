import check
from typing import Any
   
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

def higher_population(c1: Country, c2: Country) -> Country:
  '''
  Returns the country of c1 and c2 with
  the higher population (c1 if tied)
  
  Example:
     canada = Country("North America", "Trudeau", 37742157)
     india = Country("Asia", "Modi", 1380004385)
     higher_population(canada, india) => india
  '''

  if c1.population >= c2.population:
    return c1
  else:
    return c2

  pass

canada = Country("North America", "Trudeau", 37742157)
india = Country("Asia", "Modi", 1380004385)
check.expect("T1", higher_population(canada, india), india)