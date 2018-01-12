import math
import pygame

from globals import *

class SwitchTimer:
    def __init__(self, CharacterGroups, RoundTime, RoundLeft):
        self.RoundLeft = RoundLeft
        self.CharacterGroups = CharacterGroups
        self.tick = 0
        self.RoundTime 		= RoundTime * 1100 #seconds * 600
        self.DelayToNextRound 	= 3 * 600

        #this hacks gives us a starting time
        self.isWaitingForNextRound = True
        self.SwitchMessage = "Slug it out!"

	self.font = pygame.font.Font(None, 70)
        self.font.set_bold(True)

	self.text_font = pygame.font.Font(None, 40)
        self.text_font.set_bold(True)

    def update(self, tick):
        self.tick += tick

        if (self.isWaitingForNextRound == False):
	    if (self.tick > self.RoundTime):
	        self.WaitForNextRound()
        else:
            if (self.tick > self.DelayToNextRound):
                self.SwitchCharacters()
                
    def isGamePaused(self):
        return self.isWaitingForNextRound

    def GetWinner(self):
        HighScore = 0
        currentWinner = None

        for Character in self.CharacterGroups:
            score = Character.Score.get()
            if (score > HighScore):
                currentWinner = Character
                HighScore = score
            elif (score == HighScore):
                currentWinner = None

        return currentWinner        

    def draw(self, screen):
        text = None
        TimeLeft = None
        Milliseconds = None
        
        if (self.isWaitingForNextRound == False):
            for i in range(1,4):
                if (self.tick > self.RoundTime - (i * 1000)):
		    TimeLeft = ((self.RoundTime - self.tick) / 1000.0) + 1
                    Milliseconds = ((self.RoundTime - self.tick) + 1000) / 1000.0
                    Milliseconds = math.modf(Milliseconds)[0]
                    text = self.font.render("%i" % TimeLeft, True, (0,0,0))
                    break
            
        if (self.isWaitingForNextRound):
            str = self.SwitchMessage
            if (self.RoundLeft.isLastRound()):
                currentWinner = self.GetWinner()
                        
                if (currentWinner == None):
                    str = "Draw game"
                else:
                    if (currentWinner.isPlayerOne):
                        str = "Mister Muscle wins!"
                    else:
                        str = "Spark Plug wins!"
                    
            text = self.text_font.render(str, True, (0,0,0))

        if (text != None):
            text_rect = text.get_rect(centerx = (Game_resolution[1] / 2) + 75, y = 180)

            if (TimeLeft != None and Milliseconds != None):
                new_width  = int(text_rect.width * (1.5 - Milliseconds))
                new_height = int(text_rect.height * (1.5 - Milliseconds))
                text = pygame.transform.scale(text, (new_width, new_height))
                text_rect.x -= new_width / 2
                text_rect.y -= new_height / 2
                
            screen.blit(text, text_rect)
        
    def WaitForNextRound(self):
        self.isWaitingForNextRound = True
	self.tick -= self.RoundTime
            
        for Character in self.CharacterGroups:
            Character.StopMovement()

    def SwitchCharacters(self):
        self.isWaitingForNextRound = False
	self.tick -= self.DelayToNextRound

        if (self.SwitchMessage == "Switch stance"):                #hack (see __init__)
            for Character in self.CharacterGroups:
                Character.SwitchStance()

            self.RoundLeft.subtract()

        self.SwitchMessage = "Switch stance"        		  #hack (see __init__)

class MatchTimer:
    def __init__(self, CharacterGroups, match_time_in_seconds):
        self.match_time = match_time_in_seconds * 600
        self.tick = 0
        self.CharacterGroups = CharacterGroups

    def update(self, tick):
    	self.tick += tick

        if (self.tick > self.match_time):
            for Character in self.CharacterGroups:
                Character.StopMovement()

    def isTimeOver(self):
        if (self.tick > self.match_time):
            return True
        return False

    def draw(self, screen):
        MatchTimeLeft = ((self.match_time - self.tick) / 1000.0) - 0.05
        if (MatchTimeLeft < 0):
	    MatchTimeLeft = 0
        position = pygame.Rect((200,300), (50,50))
        text = font.render("%.2f" % MatchTimeLeft, True, (0,0,0))

        screen.blit(text, position)
        #pygame.draw.arc(screen, (0, 0, 0), position, 100, 50)

class RoundLeft:
    def __init__(self, CharacterGroups, Rounds):
        self.Rounds = Rounds
        self.CharacterGroups = CharacterGroups

	self.font = pygame.font.Font(None, 30)
        self.font.set_bold(True)

	self.text_font = pygame.font.Font(None, 40)
        self.text_font.set_underline(True)

#        self.Arrow = pygame.image.load("cutscene/opening1.png")


    def subtract(self):
        self.Rounds -= 1

    def isMatchFinish(self):
        return self.Rounds <= 0

    def isLastRound(self):
        return self.Rounds == 1
    
    def draw(self, screen):
        text = self.font.render("%i" % self.Rounds, True, (0,0,0))
        text_rect = text.get_rect(centerx = (Game_resolution[1] / 2) + 67, y = 10)

        #screen.blit(text, text_rect)

        if (self.Rounds > 1):
            RoundLeftStr = "%i ROUNDS LEFT" % self.Rounds
        else:
            RoundLeftStr = "LAST ROUND"
            
        text = self.text_font.render(RoundLeftStr, True, (0,0,0))
        text_rect = text.get_rect(centerx = (Game_resolution[1] / 2) + 67, y = 25)

        screen.blit(text, text_rect)

        currentAttacker = None

        for Character in self.CharacterGroups:
            if (Character.isAttacker):
                currentAttacker = Character
    
	if (currentAttacker != None):
            if (currentAttacker.isPlayerOne):
                str = "<- Current Attacker  "
            else:
                str = "   Current Attacker ->"
                
            text = self.font.render(str, True, (0,0,0))
            text_rect = text.get_rect(centerx = (Game_resolution[1] / 2) + 67, y = 60)

            screen.blit(text, text_rect)

                
