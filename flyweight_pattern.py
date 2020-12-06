import json
from typing import Dict

class Flyweight():
  """ This program is a simulation of a Turkish sports app 'Mackolik', Matcholic in our case. It has a player database for many sport types. This flyweight example, tries to create a similar table for soccer players of a certain soccer club called Bayern Munchen. There are two different types of information stored per player, them being the common information and personal information. """

  def __init__(self, common_infos: str) -> None:
    self._common_infos = common_infos

  def operation(self, personal_infos: str) -> None:
    c = json.dumps(self._common_infos)
    p = json.dumps(personal_infos)
    print(f"Database: Showing common information ({c}) and personal information ({p}).", end="")


class FlyweightFactory():
  """ This flyweight factory is able to update existing players in the database, or if no players with the specified information is found, able to create new players. It also ensures that common information is shared correctly. """

  _flyweights: Dict[str, Flyweight] = {}

  def __init__(self, initial_flyweights: Dict) -> None:
    for info in initial_flyweights:
      self._flyweights[self.get_key(info)] = Flyweight(info)

  def get_key(self, info: Dict) -> str:
    """ Returns a player's string hash for a given information. """

    return " - ".join(info)

  def get_flyweight(self, common_infos: Dict) -> Flyweight:
    """ Returns an existing player with a given information or creates a new one. """

    key = self.get_key(common_infos)

    if not self._flyweights.get(key):
      print("Database: Can't find the specified player, creating a new profile.")
      self._flyweights[key] = Flyweight(common_infos)
    else:
      print("Database: Updating an existing player profile.")

    return self._flyweights[key]

  def list_flyweights(self) -> None:
    count = len(self._flyweights)
    print(f"Database: There are {count} players:")
    print("\n".join(map(str, self._flyweights.keys())), end="")


def add_player(factory: FlyweightFactory, nationality: str, birth_date: str, name: str, position: str, number: str) -> None:
    print("\n\nAdmin: Adding a player to Matcholic app.")
    flyweight = factory.get_flyweight([number, name, position])
    flyweight.operation([nationality, birth_date])


if __name__ == "__main__":
  """ This is the main function to create a pre-populated player database then lists the players. Then updates a player which already exists in the database, then adds a new player. """

  factory = FlyweightFactory([
    [" 6", "Joshua Kimmich    ", "Right Back"],
    ["25", "Thomas Muller     ", "Offensive Midfield"],
    [" 1", "Manuel Neuer      ", "Goal Keeper"],
    ["10", "Leroy Andreas Sane", "Right Winger"],
    [" 7", "Serge Gnabry      ", "Left Winger"],
    [" 4", "Niklas Sule       ", "Centre Back"]])

  print("")

  factory.list_flyweights()

  add_player(factory, "German", "01.11.1996", "Leroy Andreas Sane", "Right Winger", "10")
  add_player(factory, "Polish", "08.21.1988", "Robert Lewandovski", "Centre Forward", "19")

  print("\n")

  factory.list_flyweights()

  print("")
