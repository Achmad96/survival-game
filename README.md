# Survival Game

## Installation

### Prerequisites

- Python 3.x installed on your system
- pynput library (for keyboard input handling)

### Installation Steps

1. Clone or download this repository to your local machine
2. Navigate to the survival-game directory:
   ```
   cd path/to/survival-game
   ```
3. Install required dependencies:
   ```
   pip install pynput
   ```

## Game Guide

### Starting the Game

Run the game with:

```
python Main.py
```

### Objective

Survive and defeat all enemies on the game board. You win when all enemies are eliminated, and lose if your health drops to zero or below.

### Game Elements

- **P**: Player character (You)
- **Z**, **S**, **C**: Different types of enemies with varying health and power levels
- **H**: Healing places that restore your health

### Controls

Use the arrow keys to move your character:

- ↑ (Up Arrow): Move up
- ← (Left Arrow): Move left
- ↓ (Down Arrow): Move down
- → (Right Arrow): Move right

### Gameplay Mechanics

1. **Movement**: Navigate the board using arrow keys
2. **Combat**: Walking into an enemy automatically engages in combat
   - Your health decreases based on the enemy's power
   - The enemy is removed from the board after combat
3. **Healing**: Walking into a healing spot (H) restores some health
   - Healing amounts vary (10, 20, or 30 points)
4. **Map Expansion**: The game board expands automatically when you reach the edges

### Game Status Information

The game displays:

- Your current health and power
- Number of remaining enemies
- Win/loss messages when game conditions are met

### Tips

- Prioritize finding healing spots if your health is low
- Plan your route to avoid multiple enemies when health is critical
- The game board expands as you move toward the edges, revealing new areas with more enemies and healing spots

## Troubleshooting

- If the game doesn't respond to arrow keys, ensure the game window is in focus
- If you encounter display issues, try adjusting your terminal/console window size
