import pygame
import math
import random
import sys

sys.path.append("./modules")

from globals import *
from game import *

CurrentState = "character select"
CurrentState = "battle"
CurrentState = "cutscene"

Game = Game()

while True:
    GameClock.tick(60)
    tick = GameClock.get_time()

    screen.fill((0, 0, 0))

    EventList = pygame.event.get()
    for Event in EventList:
        if Event.type == pygame.QUIT:
            sys.exit()

    StateMachine = (
        		("cutscene", Game.BeginningCutscene, "title screen - 1st run"),
        		("title screen - 1st run", Game.TitleScreen, "tutorial"),
        		("tutorial", Game.Tutorial, "character select"),
        		("title screen", Game.TitleScreen, "character select"),
        		("character select", Game.CharacterSelect, "load battle"),
        		("load battle", Game.LoadBattle, "battle"),
        		("battle", Game.BattleScreen, "title screen"),
        		("winscreen1", Game.WinningScreen1, "title screen"),
        		("winscreen2", Game.WinningScreen2, "title screen")
                    )

    for State in StateMachine:
        if State[0] == CurrentState:
            Result = State[1](tick, EventList)
            if (Result == "done"):
                CurrentState = State[2]
                break
            if (Result == "winner1"):
                CurrentState = "winscreen1"
                break
            if (Result == "winner2"):
            	CurrentState = "winscreen2"
                break
            
    pygame.display.flip()
