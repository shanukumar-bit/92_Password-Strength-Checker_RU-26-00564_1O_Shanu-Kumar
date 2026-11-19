# Password Strength Checker

**PS No.:** 92

**Language:** Python 3

## Project Description

This program checks a password against five security rules and classifies it as Weak, Medium, or Strong. It also provides suggestions to improve the password.

## Security Rules

One point is given for each rule:

1. Length must be at least 8 characters.
2. Must contain an uppercase letter.
3. Must contain a lowercase letter.
4. Must contain a digit.
5. Must contain a special character (@, #, $, %, &, *, !).

## Password Classification

- 0-2 points: Weak
- 3-4 points: Medium
- 5 points: Strong

Empty passwords and passwords containing spaces are rejected.

## Requirements

- Python 3
- re module
- unittest module for testing

No third-party packages are required.

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

Enter a password when prompted.

## How to Run Tests

Run:

```bash
python -m unittest test_main.py
```

The tests cover weak, medium, empty, space-containing, and strong passwords.