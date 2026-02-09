# Assignment 3

## Run
From this folder:

- `python3 -m pip install pygame` OR `pip install -r requirements.txt`
- `python3 main.py`

## Controls

### Player movement
- Arrow keys / WASD / IJKL : move player
- `P`: toggle platformer mode (jump + gravity)

### Actions
- `Space`: jump (platformer mode)
- `Left Shift / Right Shift`: dash / cooldown
- `G` : Ground Pound (platformer mode, must be airborne, cooldown 1s)

### System 
- `1` / `2` / `3`/ `4`/ `5`: feel preset (tight/floaty/heavy)
- `C`: cycle control scheme (WASD / arrows / IJKL)
- `F1`: toggle debug overlay
- `Tab`: cycle boundary mode (clamp/wrap/bounce)
- `R`: reset
- `Space`: start (from title)
- `Esc`: quit


## Added Features

1. Input Mapping class (input_mapper.py)
- InputMapper class decouples key bindings from game logic
- Actions defined as enums: MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, JUMP, DASH, GROUND_POUND (input_action.py)
- Game code reference actions instead of hardcoded keys
- Refactoring controls can be done easily without any changes to the game code.

2. Ground Pound Discrete Action
- Triggered by G key (KEYDOWN)
- Constraints:
    - Only works in platformer mode
    - Must be airborne (cannot ground pound on ground)
    - 1.0-second cooldown
    - Cannot be triggered while player on teh ground
-  Applies strong downward velocity (1200.0) when activated

3.  Debug prints show when action triggers (if F1 enabled)
4.  Debug + Console Displays Ground Pound status  Ready/Cooldown
5. Control Feel Tuning:
- Five feel presets in total; three primary presets documented below
- Each preset changes: acceleration, max speed, friction, gravity, and jump speed
- Demonstrates distinct gameplay experiences


## Control feel tuning
- `tight`: Very responsive and controlled. The character stops quickly and feels precise.
- `floaty`: Light and airy movement. The character stays in the air longer and feels softer.
- `heavy`: Strong and weighty. The character falls fast and feels grounded.
- `slow_floaty`: Slow on the ground but light in the air. Movement feels relaxed and gentle.
- `fast` : Quick and sharp. The character accelerates fast and reacts instantly.
