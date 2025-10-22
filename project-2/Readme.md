# Rock-Paper-Scissors-Lizard-Spock Game

![Rock-Paper-Scissors-Lizard-Spock](https://via.placeholder.com/800x200?text=Rock-Paper-Scissors-Lizard-Spock)  
*(A fun twist on the classic game, inspired by The Big Bang Theory! 🖖)*

## Description
This is a Python-based implementation of the expanded "Rock-Paper-Scissors-Lizard-Spock" game. It's a 6-round battle against the computer where you choose from 5 options: **rock**, **paper**, **scissors**, **lizard**, or **spock**. The game follows the unique winning rules:
- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

The first player to have more points after 6 rounds wins! Ties give points to both. Invalid inputs give the computer a free point.

Built with Python 3.x and the `random` library. No external dependencies needed.

## Features
- Interactive console-based gameplay
- Random computer opponent
- Detailed win/loss messages (e.g., "Scissors cuts paper! You Won!")
- Input validation (lowercase and stripped for ease)
- Final score summary and winner declaration
- Easy to extend (e.g., add more rounds or multiplayer)

## Installation & Setup
1. **Clone the Repo**:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the Game**:
   - Ensure Python 3 is installed (`python --version` to check).
   - Execute the script:
     ```
     python main.py
     ```
   - Follow the on-screen instructions. Enter your choice each round!

No pip installs required – it's pure Python!

## How to Play
1. Run `python main.py`.
2. Read the rules printed at the start.
3. For each of 6 rounds, type: `rock`, `paper`, `scissors`, `lizard`, or `spock`.
4. See the computer's choice and the result.
5. After 6 rounds, check the final score!

**Pro Tip**: Mix up your choices to beat the random computer. Live long and prosper! 🖖

## Game Rules Quick Reference
| Your Choice | Beats | Loses To |
|-------------|-------|----------|
| **Rock** | Lizard, Scissors | Paper, Spock |
| **Paper** | Rock, Spock | Scissors, Lizard |
| **Scissors** | Paper, Lizard | Rock, Spock |
| **Lizard** | Spock, Paper | Rock, Scissors |
| **Spock** | Scissors, Rock | Lizard, Paper |

## Contributing
- Fork the repo and create a pull request for improvements (e.g., GUI version with Tkinter, more rules, or multiplayer).
- Report bugs by opening an issue.

## License
This project is licensed under the MIT License – feel free to use and modify!

## Credits
- Original concept from *The Big Bang Theory* (Sheldon Cooper's rules).
- Code developed with help from Grok (xAI) for debugging and enhancements.
- Your name here: M. Anzal (the creator!).

---

*Last Updated: October 22, 2025*  
Questions? Open an issue or reach out! 🚀