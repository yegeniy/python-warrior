from pythonwarrior.turn import Turn
import random
import uuid
import os

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
    # Note that Turn was modified to include available abilities...
    a = random.choice(list(turn.abilities.keys()))
    # TODO: These aren't the only possible args...
    # if DEBUG: print(turn.abilities)
    directions = ["'forward'", "'backward'", "'right'", "'left'"]#, "'up'"]
    d = random.choice(directions)
    # TODO: known (latest?) spaces should be saved and direction_of(Space)
    # should be implemented somehow... Is this possible even?
    if a in ["rest_", "listen", "health", "explode_", "direction_of_stairs"]:
      return f"i.{a}()"
    else:
      return f"i.{a}({random.choice(directions)})"

class FollowGivenLog:
  FNAME = f"{os.getcwd()}/logs/25b14abd289c4c96a8d8fe920d876bdb_29"
  def __init__(self):
  # if DEBUG:
    self.actions = []
    with open(FollowGivenLog.FNAME) as l:
      for line in l.readlines():
        # print(line)
        for a_r in line.split(" : ")[1].split(" , "):
          # print(a_r)
          self.actions.append(a_r.split(" ")[0])
    self.i = 0
    if DEBUG: print(self.actions)
  def decide(self, turn: Turn):
    # with open(FollowGivenLog.FNAME) as l:
      # turns = l.readlines()
      # a = turns[self.turn_ct-1].split(" : ")[1].split(",")[-1].split(" ")[1]
    a = self.actions[self.i]
    # print(a)
    self.i += 1
    return a

# class Player(FollowGivenLog):
class Player(DecideRandomly):
  def log(self, msg):
    with open(self.fname, "a+") as log:
      log.write(msg)

  def __init__(self):
    super(Player, self).__init__()
    self.turn_ct = 1
    self.fname = f"{os.getcwd()}/logs/{uuid.uuid4().hex}"
    print(self.fname)
    # self.log(f"Turn {self.turn_ct} : ")

  def play_turn(self, i: Turn):
    # random_action
    # try:
    action = ""
    self.log(f"Turn {self.turn_ct} : ")
    while "_(" not in action:
      action = f"{self.decide(i)}"
      self.log(f"{action} ")
      # if DEBUG: print(self.log)
      self.log(f"{eval(action)} ")
      if "_(" not in action: self.log(", ")
    self.turn_ct += 1
    self.log(".\n")

    if DEBUG:
      with open(self.fname) as log: print(log.read())
    # except AttributeError:
      # self.play_turn(turn)
