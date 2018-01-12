import pygame

class Animation():
    def __init__(self,
                 base_dir,
                 animation_list_idle, animation_speed_idle,
                 animation_list_overhead, animation_speed_overhead,
                 animation_list_uppercut, animation_speed_uppercut,
                 animation_list_blockup, animation_speed_blockup,
                 animation_list_blockdown, animation_speed_blockdown,
                 animation_list_reelup, animation_speed_reelup,
                 animation_list_reeldown, animation_speed_reeldown,
                 inverted):
        
        self.animation_list = { }
        self.animation_speed = { }

        animation_list = {
            'idle': (animation_list_idle, animation_speed_idle),
            'overhead': (animation_list_overhead, animation_speed_overhead),
            'uppercut': (animation_list_uppercut, animation_speed_uppercut),
            'blockup': (animation_list_blockup, animation_speed_blockup),
            'blockdown': (animation_list_blockdown, animation_speed_blockdown),
            'reelup': (animation_list_reelup, animation_speed_reelup),
            'reeldown': (animation_list_reeldown, animation_speed_reeldown),
                         }

        for (name, (list, speed)) in animation_list.items():
            self.animation_list[name] = self.GenerateFrameData(base_dir, list, inverted)
            self.animation_speed[name] = speed
            
        self.current_animation       = 'idle'
        self.current_animation_speed = self.animation_speed['idle']
        self.current_animation_frame = 0

        self.current_tick = 0

    def GenerateFrameData(self, base_dir, animation_filenames, inverted):
        FrameData = list(range(len(animation_filenames)))
        for i in range(len(animation_filenames)):
            filepath = "%s/%s" % (base_dir, animation_filenames[i])
            current_frame_image = pygame.image.load(filepath)
            current_frame_image.set_colorkey(current_frame_image.get_at((0,0)))

            if (inverted):
                current_frame_image = pygame.transform.flip(current_frame_image, True, False)

            FrameData[i] = current_frame_image

        return FrameData

    def set(self, animation):
        if (animation in self.animation_list):
            self.current_animation = animation
            self.current_animation_frame = 0
            self.current_tick = 0
        else:
            print("warning: missing animation")
        
    def get(self):
        return (self.animation_list[self.current_animation])[self.current_animation_frame]

    def get_name(self):
        return self.current_animation

    def update(self, tick):
        self.current_tick += tick

        current_animation_speed = self.animation_speed[self.current_animation]

        if (self.current_tick > current_animation_speed[self.current_animation_frame]):
            self.current_tick -= current_animation_speed[self.current_animation_frame]
            self.current_animation_frame += 1
            
        if (self.current_animation_frame > len(self.animation_list[self.current_animation]) - 1):
            self.current_animation_frame = 0
