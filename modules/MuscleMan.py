from CharacterData import *

def Data():
    idle_animation_files      = ["m_01.png", "m_02.png"]
    idle_animation_speed      = [150, 370]
    random_idle_animation_files = ["m_03.png"]
    overhead_animation_files  = ["m_04.png", "m_05.png"]
    overhead_animation_speed  = [400, 700, 150]
    uppercut_animation_files  = ["m_06.png", "m_07.png", "m_08.png"]
    uppercut_animation_speed  = [550, 700, 150]
    blockup_animation_files   = ["m_10.png"]
    blockup_animation_speed   = [50, 70, 150]
    blockdown_animation_files = ["m_11.png"]
    blockdown_animation_speed = [50]
    reelup_animation_files    = ["m_13.png"]
    reelup_animation_speed    = [50]
    reeldown_animation_files  = ["m_12.png"]
    reeldown_animation_speed  = [50]

    return CharacterData("muscleman/",
                         idle_animation_files, idle_animation_speed,
                         overhead_animation_files, overhead_animation_speed,
                         uppercut_animation_files, uppercut_animation_speed,
                         blockup_animation_files, blockup_animation_speed,
                         blockdown_animation_files, blockdown_animation_speed,
                         reelup_animation_files, reelup_animation_speed,
                         reeldown_animation_files, reeldown_animation_speed)
