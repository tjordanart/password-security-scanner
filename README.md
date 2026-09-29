# Password Security Scanner

A Python-based password security utility that analyzes passwords against common security requirements through an interactive terminal interface.

**Try the scanner:** [tjordanart.com/password-scanner](https://www.tjordanart.com/password-scanner)

## Overview

Password Security Scanner evaluates a password against a set of common security requirements and provides a security score based on the criteria it meets.

The project was created to practice Python fundamentals while building a small security-focused utility involving input validation, string processing, conditional logic, loops, and terminal formatting.

The scanner performs all analysis locally while the program is running.

## Features

- Password security analysis
- Minimum length validation
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Security score calculation
- Weak, Medium, and Strong ratings
- Color-coded terminal results
- Interactive password testing loop
- Scanning animation and timed output

## Security Requirements

The scanner evaluates five criteria:

| Requirement | Description |
|---|---|
| **Length** | At least 8 characters |
| **Uppercase** | Contains at least one uppercase letter |
| **Lowercase** | Contains at least one lowercase letter |
| **Number** | Contains at least one number |
| **Special Character** | Contains at least one special character |

Each requirement that is satisfied contributes to the overall security score.

The program then calculates a percentage and assigns a rating:

- **Weak**
- **Medium**
- **Strong**

The interactive loop continues until the user enters a password that satisfies all five requirements.

## Technologies & Concepts

- **Python 3**
- `string` for accessing punctuation characters
- `time` for scanning animations and timed output
- ANSI escape codes for terminal formatting
- User input and validation
- Conditional logic
- Loops
- String processing
- Variables and data structures

## How It Works

The program accepts a password from the user and evaluates it against each security requirement.

The scanner checks for:

1. Minimum length
2. Uppercase characters
3. Lowercase characters
4. Numbers
5. Special characters

Each successful check contributes to the password's security score.

The results are then displayed in the terminal using color-coded output.

## How to Run

### Requirements

- Python 3
- No external dependencies

### Clone the Repository

```bash id="x9sk3d"
git clone https://github.com/Tjordanart/password.git
```

### Navigate to the Project

```bash id="j7x9cr"
cd password
```

### Run the Scanner

```bash id="k0s8wj"
python password_checker.py
```

The program will prompt you to enter a password and display the results of the security analysis.

## Future Improvements

Potential future enhancements include:

- Password entropy calculations
- More detailed strength analysis
- Common password detection
- Password recommendations
- Secure password generation
- Additional security requirements
- Password scan history
- More advanced security scoring

## What I Practiced

This project provided practice with:

- Python programming fundamentals
- User input handling
- Input validation
- Conditional statements
- Loops
- String methods
- Data structures
- Program flow
- Terminal formatting
- Building a small security-focused application

## Disclaimer

Password Security Scanner is an educational password analysis tool.

It does not store or transmit passwords. Passwords are analyzed locally while the program is running.

The scanner uses basic rule-based checks and should not be considered a comprehensive measure of real-world password security.

## Author

**Tyler Jordan**

Computer Engineering Student & Creative Technologist

[GitHub](https://github.com/Tjordanart)  
[Portfolio](https://www.tjordanart.com)
