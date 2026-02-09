from enum import Enum

class Action(str,Enum):

    # Movement continuos actions
    MOVE_LEFT = "move_left"
    MOVE_RIGHT = "move_right"
    MOVE_UP = "move_up"
    MOVE_DOWN = "move_down"

    # Discrete actions 
    JUMP = "jump"
    DASH = "dash"

    GROUND_POUND = "ground_pound"
