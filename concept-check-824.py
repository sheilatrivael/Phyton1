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

def leader_most_populous(loc: list[Country]) -> str:
  '''
  Returns the leader of the country in loc with
  the highest population (leftmost highest population if tied)
  
  Requires: loc is non-empty
  
  Example:
     canada = Country("North America", "Trudeau", 37742157)
     india = Country("Asia", "Modi", 1380004385)
     leader_most_populous([canada, india]) => "Modi"
  '''
  ans = loc[0] #canada
  for country in loc:
    if country.population > ans.population: #if india.population > canada.pop
      ans = country
  return ans.leader
  pass

canada = Country("North America", "Trudeau", 37742157)
india = Country("Asia", "Modi", 1380004385)
check.expect("T1", leader_most_populous([canada, india]), "Modi")