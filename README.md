# Tetris Game

A classic Tetris implementation in Python using Pygame, featuring various blocks, scoring, sound effects, and a ghost block preview.

## Features

- **Classic Tetris Mechanics**: Drop and rotate blocks (L, J, I, O, S, T, Z) to clear lines.
- **Score & High Score System**: Track your score and compete for the highest score.
- **Ghost Block Preview**: Visualize where the current block will land.
- **Sound Effects & Music**: Background music and sound effects for rotations and line clears.
- **Game Over Screen**: Restart or exit the game with intuitive controls.
- **Transparency Effects**: Visual feedback when locking blocks into place.

---

## Getting Started

### Prerequisites

- Python 3.x+
- Pygame

Install dependencies:

```
pip install pygame

```

### Cloning

Clone the repository:

```
git clone https://github.com/Ashish-Reddy-T/Tetris-game.git
```

Navigate into the directory and start coding:

```
cd Tetris-game
```

### Add Assets

- Place sound files (`.ogg`) and the font file (`Monogram Font.ttf`) in the correct directory (adjust paths in `game.py` and `main.py` if needed).

---

## Usage

- **Left Arrow / A**: Move block left.
- **Right Arrow / D**: Move block right.
- **Down Arrow / S**: Move block down faster.
- **Up Arrow / W**: Rotate block.
- **Space / Enter**: Restart the game after game over.
- **Escape**: Quit the game (at any point in time).

---

## Project Structure

| **File**          | **Description**                                               |
| ----------------- | ------------------------------------------------------------- |
| `color.py`        | Defines color constants used in the game.                     |
| `blocks.py`       | Contains classes for all Tetris blocks (L, J, I, O, S, T, Z). |
| `game.py`         | Manages game logic, scoring, sound, and block movement.       |
| `grid.py`         | Handles the grid layout and line-clearing mechanics.          |
| `main.py`         | Entry point; handles rendering, controls, and the game loop.  |
| `parent_block.py` | Base class for all Tetris blocks.                             |
| `position.py`     | Represents grid positions for block cells.                    |

---

## Future Improvements

- Add difficulty levels with increasing speed.
- Implement a pause feature.
- Include a scoring multiplier for combos.
- Add a preview for the next 2-3 blocks instead of one.

---

## Screenshots

![ScreenShot1](/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Pic1.png)
![ScreenShot2](/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Pic2.png)
![ScreenShot3](/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/EndGame.png)

---

## Credits

- Sound effects and music: [Sypros](https://assetstore.unity.com/packages/audio/music/black-swan-vs-white-swan-audio-pack-219984) (update path in required files).
- Monogram font: [Download link](https://www.dafont.com/monogram.font) (update path in `main.py`).

---

## Troubleshooting

- **Missing Sounds/Font**: Ensure files are placed in the correct directory and paths in `game.py`/`main.py` are updated.
- **Pygame Errors**: Reinstall Pygame if you encounter rendering issues (`pip uninstall pygame && pip install pygame`).

---

#### Enjoy the game! Contributions and feedback are welcome!
