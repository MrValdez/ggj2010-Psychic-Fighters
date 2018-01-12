from CharacterData import *

def Data():
    idle_animation_files      = ["s_01.png", "s_02.png"]
    idle_animation_speed      = [150, 370]
    random_idle_animation_files = ["s_03.png"]
    overhead_animation_files  = ["s_07.png", "s_08.png", "s_09.png"]
    overhead_animation_speed  = [550, 200, 1050]
    uppercut_animation_files  = ["s_04.png", "s_05.png", "s_06.png"]
    uppercut_animation_speed  = [540, 200, 1500]
    blockup_animation_files   = ["s_12.png"]
    blockup_animation_speed   = [50, 70, 150]
    blockdown_animation_files = ["s_13.png"]
    blockdown_animation_speed = [50]
    reelup_animation_files    = ["s_10.png"]
    reelup_animation_speed    = [50]
    reeldown_animation_files  = ["s_11.png"]
    reeldown_animation_speed  = [50]

    return CharacterData("slimdude",
                         idle_animation_files, idle_animation_speed,
                         overhead_animation_files, overhead_animation_speed,
                         uppercut_animation_files, uppercut_animation_speed,
                         blockup_animation_files, blockup_animation_speed,
                         blockdown_animation_files, blockdown_animation_speed,
                         reelup_animation_files, reelup_animation_speed,
                         reeldown_animation_files, reeldown_animation_speed)
