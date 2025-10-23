# Math Quiz Game

![Math Quiz](https://via.placeholder.com/800x200?text=Math+Quiz+Game)  
*(A fun Python-based math quiz to test your arithmetic skills! ➗✨)*

## Description
This is an interactive **Math Quiz Game** built in Python. It generates random arithmetic problems (addition, subtraction, multiplication, division) with numbers between 1 and 10. Answer correctly to keep your streak going – get one wrong, and the game ends with your score! Division results are rounded to 3 decimal places for precision.

- **Core Logic**: Uses `random` for problems, `operator` module for calculations, and input validation to handle invalid entries (e.g., letters instead of numbers).
- Pure Python 3.x – no external libraries beyond built-ins. Perfect for practicing loops, try-except, and functions!

The game continues until a wrong answer, then displays your final score (e.g., "3 out of 4").

## Features
- Randomly generated problems across 4 operations (+, -, *, /)
- Input validation with retry prompts for non-numeric entries
- Streak-based scoring (correct answers in a row)
- Clear feedback: "Correct! 🎉" or "Wrong answer! 😔"
- Rounded division results for accuracy
- Infinite play until failure (easy to modify for fixed rounds)

## Installation & Setup
1. **Clone the Repo** (add to your mini-projects folder):
   ```
   git clone https://github.com/Anzal-Developer/mini-python-project.git
   cd mini-python-project  # Navigate to your project folder, e.g., project-4
   ```

2. **Run the Game**:
   - Ensure Python 3 is installed (`python --version`).
   - Save the code as `math_quiz.py` and execute:
     ```
     python math_quiz.py
     ```
   - Start answering questions right away!

## How to Use
1. Run `python math_quiz.py` – welcome message appears.
2. For each problem (e.g., "What is 5 + 3?"), enter your answer as a number.
3. If invalid (e.g., "abc"), it'll prompt again: "Invalid input! Please enter a number."
4. Correct? Score increases, next problem. Wrong? Game over with score.
   
**Pro Tip**: Division might need decimals (e.g., 10 / 3 = 3.333) – type precisely!

## Example Output
```
Welcome to Math Quiz! Answer correctly to keep going. Wrong = game over.
What is 5 + 3?
Your answer: 8
Correct! 🎉
What is 7 * 2?
Your answer: 14
Correct! 🎉
What is 4 / 2?
Your answer: 3
Wrong answer! 😔
Your final score is 2 out of 3.
```

## Improvements Ideas
- Add difficulty levels (e.g., larger numbers or timed answers).
- Fixed number of questions (e.g., 10 rounds) instead of streak.
- High score tracking (save to file).
- GUI with Tkinter for visual appeal.
- More operations (e.g., exponents with `**`).

## Contributing
Fork the repo, fix bugs or add features (like levels), and open a pull request. Share your math twists!

## License
MIT License – free to use and modify!

## Credits
- Created by: M. Anzal (Anzal-Developer)


---

*Last Updated: October 23, 2025*  
Questions? Star the repo or drop a comment! 🚀🐍