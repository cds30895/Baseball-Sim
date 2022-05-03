#Baseball Sim

import random

print("Play Ball!")

outs = 0
inning = 1
atbat = 1
score = [0, 0]
battingorder1 = 0
battingorder2 = 0
hit = False

#Define a class of batter with a randomly
#assigned batting average for each,
#weighted toward the middle.  Set
#baserunning to 0.

class Batter:
    def __init__(self):
        self.base = 0
        self.strikes = 0
        self.balls = 0
        self.hit = False
        batavchance = random.randint(1,10)
        if batavchance <= 3:
            self.batav = (random.randint(170,220))/1000
        if batavchance > 3 and batavchance <= 9:
            self.batav = (random.randint(220, 350))/1000
        elif batavchance == 10:
            self.batav = (random.randint(350,400))/1000

#Define pitching with chances for balls,
#strikes, hits, and home runs.  Detect
#the outcome, and set base to 4 if home run.

    def pitch(self):
        hitchance = (random.randint(1,100)) / 100
        if hitchance > (self.batav + .3):
            self.strikes += 1
            if self.strikes < 3:
                print("Strike!  The count is " + str(self.balls) + " balls, " + str(self.strikes) + " strikes, " + str(outs) + " outs.")
            if self.strikes == 3:
                print("Strike 3!")
        if hitchance > self.batav and hitchance <= (self.batav + .3):
            self.balls += 1
            print("Ball " + str(self.balls) + "!  The count is " + str(self.balls) + " balls, " + str(self.strikes) + " strikes, " + str(outs) + " outs.")
        if hitchance <= self.batav and hitchance > (self.batav * .1):
            self.hit = True
            whichbase = random.randint(1,10)
            if whichbase >= 6 and whichbase <= 8:
                self.base = 1
                print("A double!")
            if whichbase > 8:
                self.base = 2
                print("A triple!")
        if hitchance <= (self.batav * .1):
            print("Home Run!")
            self.base = 4
            self.hit = True

#Define a function to advance the batting order
def advancetheorder(atbat):
    global battingorder1
    global battingorder2
    if atbat == 1:
        if battingorder1 < 8:
            battingorder1 += 1
        elif battingorder1 == 8:
            battingorder1 = 0
    elif atbat == 2:
        if battingorder2 < 8:
            battingorder2 += 1
        elif battingorder2 == 8:
            battingorder2 = 0

#Define a function to manage baserunning.
#If there is a hit, check the whole batting
#order to see if anyone is on base.  Advance
#the runners with 30% chance of being tagged
#out, and score and reset the runners
#who made it to home base.
def runthebases():
    global outs
    for i in range(9):
        if batters1[i].base > 0 and batters1[i].base != 4:
            batters1[i].base += 1
            if random.randint(1, 10) < 4:
                print("Thrown out at " + str(batters1[i].base) + " base!")
                batters1[i].base = 0
                outs += 1
        if batters2[i].base > 0 and batters2[i].base != 4:
            batters2[i].base += 1
            if random.randint(1, 10) < 4:
                print("Thrown out at " + str(batters2[i].base) + " base!")
                batters2[i].base = 0
                outs += 1
    for i in range(9):
        if batters1[i].base == 4:
            score[0] += 1
            batters1[i].base = 0
        if batters2[i].base == 4:
            score[1] += 1
            batters2[i].base = 0
  
#Define a function to reset the baserunners
#at the end of an inning.
def resetthebaserunners():
    for i in range(9):
        batters1[i].base = 0
        batters2[i].base = 0

#Define a function to report on the baserunners
def baserunningcommentary():
    firstbase = ""
    secondbase = ""
    thirdbase = ""
    for i in range(9):
        if batters1[i].base == 1 or batters2[i].base == 1:
            firstbase = " first"
        if batters1[i].base == 2 or batters2[i].base == 2:
            secondbase = " second"
        if batters1[i].base == 3 or batters2[i].base == 3:
            thirdbase = " third"
    if firstbase != "" or secondbase != "" or thirdbase != "":
        if firstbase != "" and secondbase != "" and thirdbase == "":
            secondbase = " and second"
        if firstbase != "" or secondbase != "" and thirdbase != "":
            thirdbase = " and third"
        if firstbase != "" and secondbase != "" and thirdbase != "":
            secondbase = ", second,"
        print("Runners on" + firstbase + secondbase + thirdbase + ".  " + str(outs) + " outs.\n")

#Populate the batting order for both teams in
#a list, to be cycled
batters1 = [Batter() for i in range(9)]
batters2 = [Batter() for i in range(9)]


#Main Loop - Game > Innings > Team at bat
# > Outs > Strikes
while inning <= 9:

    #After both teams bat, advance the inning
    while atbat <=2:
        if atbat == 1:
            print("\nTop of Inning " + str(inning) + " and Team 1 is up to bat!")
        if atbat == 2:
            print("\nBottom of Inning " + str(inning) + " and Team 2 is up to bat!")
        
        #Keep the inning going for 3 outs, then switch teams
        while outs < 3:
            print("\nThe score is " + str(score[0]) + " - " + str(score[1]))
            baserunningcommentary()

            #Print the batters number in the order and batting average
            if atbat == 1:
                print("\nBatting for Team 1, Batter Number " + str(battingorder1 + 1) + ", with a batting average of " + str(batters1[battingorder1].batav))
            elif atbat == 2:
                print("\nBatting for Team 2, Number " + str(battingorder2 + 1) + ", with a batting average of " + str(batters2[battingorder2].batav) + ".\n")
            
            #Pitch to the batter until 3 strikes, 4 balls, or a hit
            while hit == False:
                #input("Press ENTER to pitch.")
                if atbat == 1:
                    batters1[battingorder1].pitch()
                    if batters1[battingorder1].hit == True and batters1[battingorder1].base == 4:
                        hit = True
                        batters1[battingorder1].hit = False
                        runthebases()
                        break
                    if batters1[battingorder1].hit == True and batters1[battingorder1].base == 0:
                        hit = True
                        batters1[battingorder1].hit = False
                        runthebases()
                        batters1[battingorder1].base += 1
                        print("Batter " + str(battingorder1 + 1) + " hit a single!")
                        break
                    if batters1[battingorder1].strikes == 3:
                        outs += 1
                        print("You're out!")
                        batters1[battingorder1].strikes = 0
                        batters1[battingorder1].balls = 0
                        break
                    if batters1[battingorder1].balls == 4:
                        print("That's a walk!")
                        batters1[battingorder1].strikes = 0
                        batters1[battingorder1].balls = 0
                        runthebases()
                        batters1[battingorder1].base += 1
                        break
                elif atbat == 2:
                    batters2[battingorder2].pitch()
                    if batters2[battingorder2].hit == True and batters2[battingorder2].base == 4:
                        hit = True
                        batters2[battingorder2].hit = False
                        runthebases()
                    elif batters2[battingorder2].hit == True and batters2[battingorder2].base != 4:
                        hit = True
                        batters2[battingorder2].hit = False
                        runthebases()
                        batters2[battingorder2].base += 1
                    if batters2[battingorder2].strikes == 3:
                        outs += 1
                        print("You're out!")
                        batters2[battingorder2].strikes = 0
                        batters2[battingorder2].balls = 0
                        break
                    if batters2[battingorder2].balls == 4:
                        print("That's a walk!")
                        batters2[battingorder2].strikes = 0
                        batters2[battingorder2].balls = 0
                        runthebases()
                        batters2[battingorder2].base += 1
                        break

            hit = False
            advancetheorder(atbat)

        outs = 0
        atbat += 1
        resetthebaserunners()

    atbat = 1
    inning += 1

print("FINAL SCORE: " + str(score[0]) + " - " + str(score[1]))