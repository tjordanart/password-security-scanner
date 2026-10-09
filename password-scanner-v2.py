import string
import time
import getpass

# Terminal colors

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Delay between security checks

SCAN_SPEED = 0.3

print("=" * 50)
print("        PASSWORD SECURITY SCANNER")
print("=" * 50)

while True:

    username = input("\nEnter a username to test: ").strip()

    password = input("Enter a password to test: ")

    print("\nStarting credential security scan...")
    time.sleep(0.5)

    print("\nStarting credential security scan...")
    time.sleep(0.5)

    # Username Analysis
    print("\nUsername Analysis")
    print("-----------------")

    print("Checking username...")
    time.sleep(SCAN_SPEED)

    if len(username) > 0:
        print(GREEN + "Username entered: Pass" + RESET)
        username_entered = True
    else:
        print(RED + "Username entered: Missing" + RESET)
        username_entered = False

    print("Checking username length...")
    time.sleep(SCAN_SPEED)

    if len(username) > 5:
        print(GREEN + "Username length: Pass" + RESET)
        username_length_pass = True
    else:
        print(RED + "Username length: Too short" + RESET)
        username_length_pass = False

    # Password Analysis
    print("\nPassword Analysis")
    print("-----------------")

    score = 0

    # Check password length
    print("Checking password length...")
    time.sleep(SCAN_SPEED)

    if len(password) >= 8:
        print(GREEN + "Minimum 8 characters: Pass" + RESET)
        score += 1
    else:
        print(RED + "Minimum 8 characters: Too short" + RESET)

    # Check uppercase
    print("Checking uppercase letters...")
    time.sleep(SCAN_SPEED)

    if any(char.isupper() for char in password):
        print(GREEN + "Uppercase letter: Pass" + RESET)
        score += 1
    else:
        print(RED + "Uppercase letter: Missing" + RESET)

    # Check lowercase
    print("Checking lowercase letters...")
    time.sleep(SCAN_SPEED)

    if any(char.islower() for char in password):
        print(GREEN + "Lowercase letter: Pass" + RESET)
        score += 1
    else:
        print(RED + "Lowercase letter: Missing" + RESET)

    # Check number
    print("Checking numbers...")
    time.sleep(SCAN_SPEED)

    if any(char.isdigit() for char in password):
        print(GREEN + "Number: Pass" + RESET)
        score += 1
    else:
        print(RED + "Number: Missing" + RESET)

    # Check special character
    print("Checking special characters...")
    time.sleep(SCAN_SPEED)

    if any(char in string.punctuation for char in password):
        print(GREEN + "Special character: Pass" + RESET)
        score += 1
    else:
        print(RED + "Special character: Missing" + RESET)

    # Calculate password score
    percentage = (score / 5) * 100

    if percentage <= 40:
        rating = "Weak"
        rating_color = RED
    elif percentage <= 80:
        rating = "Medium"
        rating_color = YELLOW
    else:
        rating = "Strong"
        rating_color = GREEN

    # Display score
    print("\n-----------------")

    print(
        "Password Security Score: "
        + rating_color
        + f"{percentage:.0f}%"
        + RESET
    )

    print(
        "Password Rating: "
        + rating_color
        + rating
        + RESET
    )

    # Final credential check
    username_valid = (
        username_entered
        and username_length_pass
    )

    password_valid = (
        percentage == 100
    )

    print("\n-----------------")

    if username_valid and password_valid:

        print(
            GREEN
            + "Credential security requirements met."
            + RESET
        )

        print("\nUsername: PASS")
        print("Password: PASS")

        print(
            "\nThe username meets both requirements "
            "and all five password requirements passed."
        )

        print("\nScan complete.")

        break

    else:

        print(
            RED
            + "Credential does not meet all security requirements."
            + RESET
        )

        print(
            "\nReview the requirements marked "
            "as missing or too short."
        )

        print("\nStarting a new scan...")

        time.sleep(1)


print("\nThank you for using Password Security Scanner.")

