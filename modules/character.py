import pygame

from globals import *
from animation import *
from shadow import *
from interpolation import *

class AttackEvent():
    def __init__(self):
        self.CurrentAttack = None
        self.DamageDealt = None

AttackEvent = AttackEvent()       

class Score:
    def __init__(self, rect, isPlayerOne):
        self.isPlayerOne = isPlayerOne
        
        self.rect = rect.copy()
        if (isPlayerOne):
	    self.rect.x += 65
        else:
            self.rect.x -= 25
            
        self.rect.y += 10
        
        self.score = 0
	self.player_font = pygame.font.Font(None, 20)
        self.player_font.set_bold(False)
        self.player_font.set_underline(True)
        
	self.score_font = pygame.font.Font(None, 30)
        self.score_font.set_bold(True)

    def add(self, score):
        self.score += score

    def get(self):
        return self.score

    def draw(self):
        if (self.isPlayerOne):
            PlayerStr = "Mister Muscle"
        else:
            PlayerStr = "Spark Plug"
            
        text = self.player_font.render(PlayerStr, True, (0,0,0))
        screen.blit(text, self.rect)
        
        rect2 = self.rect.copy()
        rect2.y += 20
        
        rect2.width = 10
        rect2.centerx = rect2.x

        text = self.score_font.render("%4i" % self.score, True, (0,0,0))
        screen.blit(text, rect2)

class Character(pygame.sprite.Sprite):
    def __init__(self, CharacterData, isPlayerOne, isAttacker):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.isPlayerOne = isPlayerOne
        self.isAttacker = isAttacker
        self.DeceptionMeter = 0
        
        self.Animation = Animation(CharacterData.base_dir,
                                   CharacterData.idle_animation_files, CharacterData.idle_animation_speed,
                                   CharacterData.overhead_animation_files, CharacterData.overhead_animation_speed,
                                   CharacterData.uppercut_animation_files, CharacterData.uppercut_animation_speed,
                                   CharacterData.blockup_animation_files, CharacterData.blockup_animation_speed,
                                   CharacterData.blockdown_animation_files, CharacterData.blockdown_animation_speed,
                                   CharacterData.reelup_animation_files, CharacterData.reelup_animation_speed,
                                   CharacterData.reeldown_animation_files, CharacterData.reeldown_animation_speed,
                                   self.isPlayerOne == False)

        self.image = self.Animation.get()
                         
        self.rect = self.image.get_rect()
        self.ResetStance()

        if (self.isPlayerOne):
            ScoreRect = pygame.Rect(0,0,100,50)
        else:
            ScoreRect = pygame.Rect(500,0,100,50)
            
        self.Score = Score(ScoreRect, self.isPlayerOne)
        
        self.current_startup_frame = 0
	self.startup_frame = 10 * 60

        self.current_recover_frame = 0
        self.recover_frame = 5 * 60

        self.current_active_frame = 0
        self.active_length = 2 * 80

	self.current_attack_cooldown = 0
        self.attack_cooldown = 100

    def update(self, tick, EventList):
        #self.DrawMeter()
        self.Score.draw()
        
        if (self.Pause):
            return
        
        self.Animation.update(tick)
        self.image = self.Animation.get()

        for event in EventList:
            if (event.type == pygame.KEYDOWN or \
               (use_gamepad and self.isPlayerOne and event.type == pygame.JOYHATMOTION)):
                
                if (self.isAttacker and \
                    (self.current_attack_cooldown > 0) or self.is_recovering):
                    continue
                
                UpKey_pushed = False
                DownKey_pushed = False

                if (self.isPlayerOne and event.type == pygame.JOYHATMOTION):
                    if (event.value[1] == 1):
                        UpKey_pushed = True
                    elif (event.value[1] == -1):
                        DownKey_pushed = True
                elif (event.type == pygame.KEYDOWN):
                    if (self.isPlayerOne):
                        UpKey = pygame.K_w
                        DownKey = pygame.K_s
                    else:
                        UpKey = pygame.K_UP
                        DownKey = pygame.K_DOWN

                    UpKey_pushed = (event.key == UpKey)
                    DownKey_pushed = (event.key == DownKey)
                
                if (self.isAttacker):
                    if (UpKey_pushed):
                        original_rect = pygame.Rect(self.original_pos, (self.rect.width, self.rect.height))
                        Shadow(self.image, original_rect, -30, self.isPlayerOne)
                        self.has_attacked = True                       
                        self.current_attack_cooldown = self.attack_cooldown
                        self.Animation.set("overhead")

                    if (DownKey_pushed):
                        has_moved_keydown = True
                        original_rect = pygame.Rect(self.original_pos, (self.rect.width, self.rect.height))
                        Shadow(self.image, original_rect, +30, self.isPlayerOne)
                        self.has_attacked = True
                        self.current_attack_cooldown = self.attack_cooldown
                        self.Animation.set("uppercut")
               	else:
                   if (UpKey_pushed):
                 	self.Animation.set("blockup")
                   if (DownKey_pushed):
                 	self.Animation.set("blockdown")
                       
        if (AttackEvent.CurrentAttack != None):
           if (AttackEvent.CurrentAttack == "overhead"):
               if (self.Animation.get_name() == "blockup"):
                   self.DeceptionMeter += 10
                   AttackEvent.CurrentAttack = "blocked"
                   self.Score.add(30)
               else:
                   if (self.isAttacker == False):
                       self.Animation.set('reelup')
                       AttackEvent.DamageDealt = 10

           if (AttackEvent.CurrentAttack == "uppercut"):
               if (self.Animation.get_name() == "blockdown"):
                   self.DeceptionMeter += 10
                   AttackEvent.CurrentAttack = "blocked"
                   self.Score.add(30)
               else:
               	   if (self.isAttacker == False):
                       self.Animation.set('reeldown')
                       AttackEvent.DamageDealt = 10

        if (self.current_attack_cooldown > 0):
	    self.current_attack_cooldown -= tick
            
	if (self.isAttacker == True):
            if (self.has_attacked == True):
                self.current_startup_frame += tick

                if (self.current_startup_frame > self.startup_frame):
                    self.has_attacked = False

                    self.is_active = True
                    self.current_active_frame = 0
                        
            if (self.is_active == True):
                self.current_active_frame += tick

                self.new_pos = Interpolation(beginning_pos = self.original_pos,
                                         end_pos = self.final_pos,
                                         current_time = self.current_active_frame,
                                         animation_length = self.active_length)
                self.rect.left, self.rect.top = (self.new_pos[0], self.new_pos[1])

                if (AttackEvent.CurrentAttack != "blocked" and \
                    self.active_length - self.current_active_frame ) < 10:
                    if (self.Animation.get_name() == "overhead"):
                    	AttackEvent.CurrentAttack = "overhead"
                    if (self.Animation.get_name() == "uppercut"):
                    	AttackEvent.CurrentAttack = "uppercut"

                    self.is_active = False
                    self.is_recovering = True
                    self.current_recover_frame = 0

            if (self.is_recovering == True):
                if (self.current_recover_frame  > self.recover_frame):
                    self.is_recovering = False
                    self.rect.left = self.original_pos[0]
                    self.rect.top = self.original_pos[1]
                    self.Animation.set("idle")
                    if (AttackEvent.CurrentAttack != "blocked"):
                    	self.Score.add(100)
                    AttackEvent.CurrentAttack = None

                    self.current_startup_frame = 0                  

                self.current_recover_frame += tick

    def DrawMeter(self):
        if (self.DeceptionMeter > 100):
            self.DeceptionMeter = 100
        MeterBar = pygame.Rect(0, 0, 0, 0)
        if (self.isPlayerOne):
	    MeterBar.left = 30
        else:
	    MeterBar.left = Game_resolution[0] - 140
            
        MeterBar.top  =  self.rect.top + self.rect.height
        MeterBar.width = 110 * (self.DeceptionMeter / 100.0)
        MeterBar.height = 10
        
        if (self.DeceptionMeter):
            per = self.DeceptionMeter / 100.0
            color = (100 * per,
                     155 * per,
                     130 * per)
            pygame.draw.rect(screen, color, MeterBar)

    def StopMovement(self):
        self.Pause = True
        
    def SwitchStance(self):
        self.ResetStance()
        self.isAttacker = not self.isAttacker

    def ResetStance(self):
        self.Pause = False
        self.Animation.set("idle")
        AttackEvent.CurrentAttack = None

        self.has_attacked = False
        self.is_recovering = False
        self.is_active = False

        DistanceFromBorder = -200

        if self.isPlayerOne:
	    self.rect.left = DistanceFromBorder
        else:
            self.rect.left = Game_resolution[0] - (DistanceFromBorder + self.rect.width)
            
        self.rect.top = 60
        
        self.original_pos = [self.rect.x, self.rect.y]
        self.final_pos = [0,0]
        if (self.isPlayerOne):
	    self.final_pos[0] = self.rect.left + 300
        else:
            self.final_pos[0] = self.rect.left - 300            
        self.final_pos[1] = self.rect.top
