from pythonwarrior.turn import Turn
import random

DEBUG = False
DEBUG = True
"""
time ./bin/pythonwarrior -d pythonwarrior/yeg-intermediate -t 0

Success! You have found the stairs.
Level Score: 12
Time Bonus: 0
Clear Bonus: 2
Total Score: 14

Sorry, you failed level 3. Change your script and try again.
"""

class DecideRandomly:
  # Random choice
  def decide(self, turn: Turn):
    # senses = []
    # abilities = ['walk_', 'attack_', 'rest_', 'rescue_', 'shoot_', 'bind_', 'detonate_']
    a = random.choice(list(turn.abilities.keys())) #list(filter(lambda a: a in available, abilities + senses)))
    # TODO: These aren't the only possible args...
    # if DEBUG: print(turn.abilities)
    directions = ["'forward'", "'backward'", "'right'", "'left'"]
    d = random.choice(directions)
    if a in ["rest_", "listen", "health", "explode_", "direction_of_stairs"]:
      return f"{a}()"
    else:
      return f"{a}({random.choice(directions)})"

class Player(DecideRandomly):
  def __init__(self):
    self.log = ""

  def play_turn(self, i: Turn):
    # random_action
    # try:
    action = ""
    while "_(" not in action:
      action = f"i.{self.decide(i)}"
      self.log += f"{action} "
      # if DEBUG: print(self.log)
      self.log += f"{eval(action)} "
    if DEBUG: print(self.log)
    # except AttributeError:
      # self.play_turn(turn)
