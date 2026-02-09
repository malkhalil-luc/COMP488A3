1. Install dependencies:
   pip install -r requirements.txt

2. Run the game:
   python main.py

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

1. Input Mapping Layer (input_mapper.py)
* - * InputMapper class decouples key bindings from game logic
* - * Actions defined as enums: MOVE_LEFT, MOVE_RIGHT, JUMP, DASH, GROUND_POUND
* - * Game references actions instead of specific keys → easier to remap controls

2. Ground Pound Discrete Action

* - * Triggered by G key (KEYDOWN)
* - * Constraints:
        - Only works in platformer mode
        - Must be airborne (cannot ground pound on ground)
        - 1.0-second cooldown
* - * Applies strong downward velocity (1200.0) when activated
* - * Debug prints show when action triggers (if F1 enabled)
* - * Debug Displays Colodown

## What to change first
- Try editing preset values in `input_control_feel/game.py`:
  - accel / friction / max speed
  - gravity / jump speed
- Try changing dash cooldown or dash impulse