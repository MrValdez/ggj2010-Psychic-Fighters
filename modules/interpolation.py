def Interpolation(beginning_pos, end_pos, current_time, animation_length):
    rect = [0, 0]
    delta = float(current_time) / float(animation_length)
        
    rect[0] = beginning_pos[0] + ((end_pos[0] - beginning_pos[0]) * delta)
    rect[1] = beginning_pos[1] + ((end_pos[1] - beginning_pos[1]) * delta)
    
    return rect
