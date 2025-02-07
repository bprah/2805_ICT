# Pac-Man Clone

A Python-based **Pac-Man** clone implemented using **Pygame**. This project features a fully playable Pac-Man game with AI-controlled ghosts, randomly generated mazes, and configurable game settings.

## 📌 Features

- 🎮 **Classic Pac-Man gameplay** with player movement, coin collection, and power-ups.
- 👻 **AI-controlled ghosts** with different behaviors (chasing, random movement, fleeing, etc.).
- 🏭 **Factory pattern** used for enemy creation.
- 🏗️ **State pattern** for game states (running, game over, win).
- 🔄 **Singleton pattern** for the player instance.
- ⚡ **Power-ups** that temporarily weaken ghosts.
- 🔀 **Random maze generation** for different playthroughs.

## 🛠 Technologies Used

- **Python** (Main programming language)
- **Pygame** (Graphics, game loop, and event handling)

## 🏗 Design Patterns Implemented

This project follows various software design patterns to improve structure and maintainability:

| **Pattern**          | **Used In**                | **Purpose** |
|----------------------|---------------------------|------------|
| **Factory Method**   | `Enemy Factory.py`        | Creates different types of enemies dynamically |
| **Singleton**        | `Player.py`               | Ensures only one player instance exists |
| **State**           | `Play.py`                  | Manages game states (running, game over, win) |
| **Strategy**        | `Enemy.py`                 | Different movement behaviors for ghosts |
| **Observer-like**   | `Play.py`                  | Responds to player actions dynamically |

## 🎓 Course Information
This project was designed for the **Griffith University Course 2805ICT - System and Software Design**.

## 🚀 Installation

### **Prerequisites**
- Python 3.x installed
- `pip install pygame`

### **Run the Game**
```bash
python StartPage.py
```

## 📂 Project Structure
```
Pac-Man-Clone/
│── Controllers/
│   ├── Play.py            # Main game logic
│── Models/
│   ├── Player.py          # Player class (Singleton)
│   ├── Enemy.py           # Enemy class (AI movement)
│   ├── Enemy Factory.py   # Factory Pattern for enemy creation
│── Views/
│   ├── Settings.py        # Game settings (screen size, colors, etc.)
│   ├── maze.py            # Random maze generator
│── Assets/                # Image and sound assets
│── StartPage.py           # Game start menu
│── README.md              # This file
```

## 🎮 Controls
- **Arrow Keys** - Move Pac-Man
- **Esc** - Quit game
- **Spacebar** - Restart after game over

## 🤝 Contributors
- **Blake Jones**
- **Jeremy McGahey**
- **Petar Vidakovic**
- **Brandon Prahaladh**

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy the game! 👾
