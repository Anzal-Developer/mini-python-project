# Address Validator

![Email Validation](https://via.placeholder.com/800x200?text=Email+Address+Validator)  
*(A simple Python tool to check if your email address is basic-valid! 📧)*

## Description
This is a lightweight Python program called **AddressValidator** that checks if a user-input string looks like a valid email address. It performs a basic validation by ensuring the input contains both an **'@' symbol** and a **'.' (dot)** – the bare minimum for most emails (e.g., "user@example.com").

- **How it works**: The program runs in a loop, prompting for email inputs until you type 'exit'. It prints "valid address" if both symbols are present, or flags missing ones with error messages.
- Built with pure Python 3.x – no libraries needed. Great for beginners learning string methods like `find()`!

**Note**: This is a super-basic checker (doesn't validate full format like regex would). Real-world use? Pair it with libraries like `email-validator` for pro-level checks.

## Features
- Interactive loop for multiple validations
- Clear error messages for missing '@' or '.'
- Easy exit with 'exit' command
- Console-based, no GUI needed

## Installation & Setup
1. **Clone the Repo** (if adding to your mini-projects):
   ```
   git clone https://github.com/Anzal-Developer/mini-python-project.git
   cd mini-python-project  # Or your project folder, e.g., project-3
   ```

2. **Run the Program**:
   - Make sure Python 3 is installed (`python --version`).
   - Save the code as `address_validator.py` and run:
     ```
     python address_validator.py
     ```
   - Enter emails like `test@gmail.com` (valid) or `test@g` (invalid) to test!

## How to Use
1. Run the script – it'll print instructions.
2. Enter an email: It must have '@' and '.' (e.g., "hello@world.com" → valid).
3. Missing '@'? → "invalid address: missing @"
4. Missing '.'? → "invalid address: missing ."
5. Type 'exit' to quit.
   
**Example Output**:
```
This program will decide if your input is a valid email address or not
An email address must contain an '@' sign and a '.' sign
Please enter an email address to validate or type 'exit' to quit: test@gmail.com
valid address
An email address must contain an '@' sign and a '.' sign
Please enter an email address to validate or type 'exit' to quit: test@invalid
invalid address: missing .
```

## Improvements Ideas
- Add regex for full email validation (e.g., using `re` module).
- Handle case-insensitivity better.
- Save valid emails to a file.
- GUI version with Tkinter!

## Contributing
Fork it, add features (like advanced checks), and submit a PR. Report issues if the basic logic trips you up!

## License
MIT License – use freely!

## Credits
- Created by: M. Anzal (Anzal-Developer)
- Inspired by basic Python string exercises.

---

*Last Updated: October 23, 2025*  
Questions? Star the repo or comment! 🚀