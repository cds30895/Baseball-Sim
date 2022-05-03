"""
Baseball Sim

Stretch Goals:
  Track win/loss based on team name, allowing more than two teams
"""
import random

winrecord = [0, 0]

"""
Batter Object
Make a batter with a passed name.
Set base to 0.
Assign weighted random batting average.
"""
class Batter:
  def __init__(self, name):
    self.name = "Batter " + str(name)
    self.base = 0
    batavchance = random.randint(1,10)
    if batavchance <= 3:
      self.batav = (random.randint(170,220))/1000
    if batavchance > 3 and batavchance <= 9:
      self.batav = (random.randint(220, 350))/1000
    elif batavchance == 10:
      self.batav = (random.randint(350,400))/1000

"""
Team Object
Make a team with a passed name and 9 batters, labeled Batter 1-9.
Set a tracker for which batter is at bat.
"""
class Team:
  def __init__(self, name):
    self.name = name
    self.batters = [Batter((i+1)) for i in range(9)]
    self.atbat = 0

"""
Game Object
Make teams with players.
Set score, inning, outs, balls, strikes, hit.
"""
class Baseballgame:
  def __init__(self):
    self.score = [0, 0]
    self.inning = 1
    self.outs = 0
    self.balls = 0
    self.strikes = 0
    self.hit = False
    self.uptobat = 0
    self.gameover = False
    team0name = str.title(input("Away Team Name: "))
    team1name = str.title(input("Home Team Name: "))
    self.teams = [Team(team0name), Team(team1name)]

  """
  Show the score for each team.
  """
  def displayscore(self):
    print(self.teams[0].name + ": " + str(self.score[0]) + ", " + self.teams[1].name + ": " + str(self.score[1]))

  """
  Show the win/loss record of each team.
  """
  def displaywinrecord(self):
    print("The " + self.teams[0].name + "'s win record is " + str(winrecord[0]) + "-" + str(winrecord[1]) + ".\n" + "The " + self.teams[1].name + "'s win record is " + str(winrecord[1]) + "-" + str(winrecord[0]) + ".\n")

  """
  End the Game
  Show the score, update and display the win record for each team.
  """
  def endgame(self):
    self.displayscore()
    if self.score[0] > self.score[1]:
      winrecord[0] += 1
    elif self.score[0] < self.score[1]:
      winrecord[1] += 1
    self.displaywinrecord()
    self.gameover = True
  
  """
  Advance the Inning for 9 innings.
  After 9 innings, end the game unless the score is tied.
  """
  def advancetheinning(self):
    if self.inning <= 8:
      self.inning += 1
    elif self.inning > 9 and self.score[0] != self.score[1]:
      self.endgame()
    elif self.inning > 9 and self.score[0] == self.score[1]:
      self.inning +=1

  """
  Switch Teams
  To be called when three outs are reached.
  """
  def switchteams(self):
    if self.uptobat == 0:
      self.uptobat += 1
      self.outs = 0
    elif self.uptobat == 1:
      self.uptobat -= 1
      self.outs = 0
      self.advancetheinning()

if __name__ == "__main__":
  playball = Baseballgame()
  print(playball.teams[0].batters[0].name)
  playball.displayscore()
  playball.inning = 9
  print(playball.inning)
  playball.score[0] += 1
  playball.displayscore()
  playball.advancetheinning()
  print(playball.inning)
  playball.endgame()
  print(winrecord)

while playball.gameover == False:
  while playball.uptobat == 0:
    while outs < 3:
    playball.switchteams()


#Start Inning Loop
  #Team 1 At Bat Loop
    #Resume Batting Order
    #Pitch To Batter Loop
      #Ball
        #Update Count
        #If 4 Balls: Add Base
      #Strike
        #Update Count
        #If 3 Strikes: Out
          #Advance Batting Order
      #Foul
        #If Strikes < 2:
          #Strike
            #Update Count
        #Elif Strikes 2:
            #Continue
      #Hit
        #Chance of Outs or 1-4 Bases
        #If Out: Advance Batting Order
        #Elif Base: Run The Bases
      #If Outs == 3:
        #Break
      #Elif Outs < 3:
        #Continue
  #Team 2 At Bat
    #Resume Batting Order
    #Pitch to Batter Loop
      #...
  #Advance the Inning
  #If Inning > 9:
    #Break
  #Elif Inning <=9:
    #Display Inning and Score
#Display Score

