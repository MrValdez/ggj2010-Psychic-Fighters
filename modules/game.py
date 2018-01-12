import pygame
import random

import globals
from character import *
from gametimer import *
import MuscleMan
import SlimDude

#Create Group
CharacterGroups = pygame.sprite.Group()
AllSprites = pygame.sprite.RenderUpdates()

Character.containers = (AllSprites, CharacterGroups)
Shadow.containers = (AllSprites)

GameClock = pygame.time.Clock()

class Cutscene:
    def __init__(self, cutscene_files, cutscene_data):
        self.cutscene 	   = cutscene_files
        self.cutscene_data = cutscene_data

    	self.cutscene_font = pygame.font.Font(None, 30)
        self.cutscene_font.set_bold(True)

        self.current_cutscene = 0
        self.cutscene_tick = 0

    def run(self, tick, EventList):
        for event in EventList:
            if (event.type == pygame.KEYDOWN):
                return "done"

        self.cutscene_tick += tick
        cutscene = self.cutscene_data[self.current_cutscene]

        if (self.cutscene_tick > (cutscene[1] * 1000)):
            self.cutscene_tick -= (cutscene[1] * 1000)
        #if (self.cutscene_tick > (1000)):
        #    self.cutscene_tick -= (1000)
            self.current_cutscene += 1
            
        if (self.current_cutscene > len(self.cutscene_data) - 1):
            return "done"

        screen.blit(self.cutscene[cutscene[0]], (0,0))

        #cutscene_y = 320
        cutscene_y = 345
        text = self.cutscene_font.render(cutscene[2], True, (255, 255, 255))
        screen.blit(text, (30, cutscene_y))
        text = self.cutscene_font.render(cutscene[3], True, (255, 255, 255))
        screen.blit(text, (30, cutscene_y + 40))
        
        
class Game:
    def __init__(self):
        self.tick = 0
        self.LoadBeginningCutscene()
        self.LoadTutorial()
        self.LoadTitleScreen()
        self.LoadCharacterSelect()
        self.LoadWinning1Cutscene()
        self.LoadWinning2Cutscene()

    def LoadBeginningCutscene(self):
        cutscene_files = (
		          pygame.image.load("cutscene/INTRO frame 1.png"),
		          pygame.image.load("cutscene/INTRO frame 2.png"),
		          pygame.image.load("cutscene/INTRO frame 3.png")
                        )
        
        cutscene_data = (
        	(0, 10, "In the near future, people with the", " abilities to see the future has appeared."),
        	(0, 13, "These people could tell what you plan to do,", " before you even attempt to do it."),
            	(0, 12, "This has caused problems for the Olympics.", " How could it be fair if your opponent..."),
                (0, 6, "...could predict the future?", ""),
        	(1, 10, "Agent I: I don't understand it. I don't", " see any cheating on this camera, either."),
        	(1, 10, "Agent I: I have to accept the facts that there", " are others who has precognition abilities..."),
                (1, 4, "Agent I: ...similar to mine", ""),
        	(2, 7, "Agent I: Well then, I just have to" , " get rid of these so called...")
            )
        
        self.BeginningCutsceneData = Cutscene(cutscene_files, cutscene_data)

    def LoadWinning1Cutscene(self):
        cutscene_files = (
		          pygame.image.load("cutscene/muscleman fight scene with AI.png"),
		          pygame.image.load("cutscene/muscleman ending frame 1.png"),
		          pygame.image.load("cutscene/muscleman ending frame 2.png"),
		          pygame.image.load("cutscene/muscleman ending frame 3.png"),
		          pygame.image.load("cutscene/muscleman intro.png"),
                        )
        
        cutscene_data = (
        	(0, 5, "Mister Muscleman defeats Agent I", "<Todo: insert ultra-awesome fight scene>"),
            	(4, 6, "At home, Mister Muscleman is", "watching his victory at the olympics"),
            	(1, 5, "Mister Muscle: Hmm, the mail is here.", "Er, what's this card?"),
            	(1, 3, "...", ""),
            	(1, 4, "Agent I sent me this card. I don't get it.", "I wonder what he wants...?"),
            	(2, 5, "Mister Muscle: What is it that you want?", " I already beaten you."),
            	(2, 6, "Agent I: I need to know. I need to know how", "you were able to deceive the psychic warriors."),
            	(2, 6, "Mister Muscle: Is that all? Look, it's real easy.", ""),
            	(2, 3, "Mister Muscle: I know that all psych warriors", "can predict my attacks."),
            	(2, 3, "So I simply feint my moves.", ""),
            	(2, 2, "...", ""),
            	(2, 1, "..........", ""),
            	(2, 1, "................", ""),
            	(2, 3, "Agent I: That's it???", ""),
            	(2, 2, "Mister Muscle: That's it.", ""),
            	(2, 3, "...................", "Agent I: Oh."),
            	(3, 1, "Agent I: Ok. Thanks.", "Byebye. Thanks for the tip.")
            )
        
        self.Win1CutsceneData = Cutscene(cutscene_files, cutscene_data)

    def LoadWinning2Cutscene(self):
        cutscene_files = (
		          pygame.image.load("cutscene/slim fight scene with AI.png"),
		          pygame.image.load("cutscene/slim intro.png"),
		          pygame.image.load("cutscene/slim ending frame 1.png"),
		          pygame.image.load("cutscene/slim ending frame 2.png")            
                        )
        
        cutscene_data = (
        	(0, 5, "Spark Plug defeats Agent I", "<Todo: insert ultra-awesome fight scene>"),
        	(2, 7, "Precognition...", " is the result of a bug in the system."),
        	(2, 7, "This... \"bug\" can help my people.", ""),
            	(3, 3, "...", ""),
                (3, 4, "I have won this \"Olympics\".", "And so I claim my prize."),
            	(1, 3, "......", ""),
            	(1, 10, "Spark Plug: This is the final solution.", "...this will help my people.")
            )
        
        self.Win2CutsceneData = Cutscene(cutscene_files, cutscene_data)

    def LoadTutorial(self):
        cutscene_files = (
		          pygame.image.load("cutscene/tutorial.png"),
		          pygame.image.load("cutscene/tutorial2.png"),
		          pygame.image.load("cutscene/tutorial3.png"),
		          pygame.image.load("cutscene/tutorial4.png")
                        )
        
        cutscene_data = (
        	(0, 3, "Tutorial", " - How to Play"),
        	(0, 4, "Psychic Fighters is a game of deception.", "The goal is to outscore your enemy."),
            	(1, 5, "The controls for Player 1 are:", " [w] for uppercut, [s] for uppercut"),
            	(2, 5, "The controls for Player 2 are:", " [Up] for uppercut, [Down] for uppercut"),
            	(2, 5, "If you start the game with a joystick inserted,", "Player 1 will be controlled by the 1st joystick."),
            	(2, 5, "Each round, an attacker is randomly chosen.", "The other player becomes a defender."),
            	(2, 3, "The attacker has %i seconds to attack." % ROUND_TIME, "Each succesful attack gives points!"),
            	(2, 2, "The defender can only defend.", "If he guesses right, he gains points."),
            	(2, 3, "After %i seconds have passed, the attacker" % ROUND_TIME, "and the defender switches."),
            	(2, 2, "The game ends after %i rounds." % NUMBERS_OF_ROUNDS, ""),
            	(3, 4, "Protip: you can press multiple buttons before", "the actual attack to confuse the enemy.")
            )
        
        self.TutorialData = Cutscene(cutscene_files, cutscene_data)

    def BeginningCutscene(self, tick, EventList):
        return self.BeginningCutsceneData.run(tick, EventList)

    def Tutorial(self, tick, EventList):
        return self.TutorialData.run(tick, EventList)

    def WinningScreen1(self, tick, EventList):
        return self.Win1CutsceneData.run(tick, EventList)

    def WinningScreen2(self, tick, EventList):
        return self.Win2CutsceneData.run(tick, EventList)
    
    def LoadTitleScreen(self):
        self.TitleScreenImage = pygame.image.load("GUI/main menu screen.png")

    	self.TitleScreen_font = pygame.font.Font(None, 30)
        self.TitleScreen_font.set_bold(True)
        
    def TitleScreen(self, tick, EventList):
        screen.blit(self.TitleScreenImage, (0,0))

        self.tick += tick
        if (self.tick < 1000):
            text = self.TitleScreen_font.render("Press ENTER", True, (255, 255, 255))
            pos = pygame.Rect((0,370), (10, 10))
            pos.centerx = (Game_resolution[0] / 2) - (self.TitleScreen_font.size("Press ENTER")[0] / 2)
            screen.blit(text, pos)

        if (self.tick > 1500):
            self.tick = 0

        for event in EventList:
            if (event.type == pygame.KEYDOWN and \
                event.key == pygame.K_RETURN):
	        return "done"

    def LoadCharacterSelect(self):
        self.MainMenuBGImage = pygame.image.load("GUI/main menu screen bg.png")
        self.CharacterSelectImage = pygame.image.load("GUI/character select.png")
        self.CharacterSelectIcon = pygame.image.load("GUI/character select glow.png")
        
    def CharacterSelect(self, tick, EventList):
        screen.blit(self.MainMenuBGImage, (0,0))
        screen.blit(self.CharacterSelectImage, (0,0))
	screen.blit(self.CharacterSelectIcon, (125,30))

        for event in EventList:
            if (event.type == pygame.KEYDOWN):
                return "done"

    def LoadBattle(self, tick, EventList):
        #Create Instance
        Attacker = random.randint(0,1)

        Character(MuscleMan.Data(), True,  Attacker == 0)
        Character(SlimDude.Data(),  False, Attacker == 1)

        self.RoundLeft = RoundLeft(CharacterGroups, NUMBERS_OF_ROUNDS)
        self.SwitchTimer = SwitchTimer(CharacterGroups, ROUND_TIME, self.RoundLeft)
        #MatchTimer = MatchTimer(CharacterGroups, 10)
        return "done"

    def BattleScreen(self, tick, EventList):
        screen.blit(background, (0,0))
    #    if not SwitchTimer.isGamePaused():
    #        MatchTimer.update(tick)

        self.SwitchTimer.update(tick)
        AllSprites.update(tick, EventList)

        AllSprites.draw(screen)
    #    MatchTimer.draw(screen)
        if (not self.RoundLeft.isMatchFinish()):
	    self.RoundLeft.draw(screen)
        self.SwitchTimer.draw(screen)

    #    if (MatchTimer.isTimeOver()):
        if (self.RoundLeft.isMatchFinish()):
	    Winner = self.SwitchTimer.GetWinner()

            AllSprites.empty()
            CharacterGroups.empty()

            if (Winner != None):
                if (Winner.isPlayerOne):
                    return "winner1"
                else:
                    return "winner2"
            
            return "done"
