Password Security Scanner

A Python-based password strength checker that analyzes password security requirements through a terminal interface.

This project was created to practice Python fundamentals including input validation, conditional logic, loops, string processing, and building a simple security-focused utility.

⸻

Features

* Password strength analysis
* Length validation
* Uppercase letter detection
* Lowercase letter detection
* Number detection
* Special character detection
* Security score calculation
* Color-coded terminal results
* Interactive password testing loop

⸻

Technologies Used

* Python 3
* string - Provides access to punctuation characters for special character checks
* time - Creates scanning animations and delays
* ANSI escape codes - Adds terminal color output

⸻

How It Works

The Password Security Scanner evaluates a password against five security requirements:

* Minimum length of 8 characters
* Contains uppercase letters
* Contains lowercase letters
* Contains numbers
* Contains special characters

Each requirement passed increases the security score. The program then calculates an overall percentage and assigns a rating:

* Weak
* Medium
* Strong

The scanner continues running until a password meets all security requirements.

⸻

How to Run

1. Make sure Python 3 is installed.
2. Clone the repository:

git clone https://github.com/Tjordanart/password.git

3. Navigate to the project folder:

cd password

4. Run the program:

python password_checker.py

⸻

Purpose of This Project

This project was created to practice:

* Python variables
* User input handling
* Loops
* Conditional statements
* Lists
* String methods
* Data validation
* Program flow
* Terminal formatting

⸻

Future Improvements

Possible additions:

* Password entropy calculation
* Estimated password strength scoring
* Common password detection
* Password suggestions
* Secure password generator
* Save scan history
* Additional security rules

⸻

Disclaimer

This project is an educational password analysis tool.

It does not store, transmit, or collect passwords. Passwords are only analyzed locally while the program is running.

⸻

Author

Created by Tyler Jordan

GitHub: https://github.com/Tjordanart