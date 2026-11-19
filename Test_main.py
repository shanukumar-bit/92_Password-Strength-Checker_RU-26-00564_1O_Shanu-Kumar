import unittest
from main import check_password


class TestPasswordStrengthChecker(unittest.TestCase):

    # Test Case 1: Normal Input (Weak)
    def test_weak_password(self):
        expected = (
            "Strength: Weak (2/5)\n"
            "Suggestions: use at least 8 characters, add an uppercase letter, add a special character"
        )
        self.assertEqual(check_password("abc123"), expected)

    # Test Case 2: Boundary / Minimum Input (Medium)
    def test_medium_password(self):
        expected = (
            "Strength: Medium (4/5)\n"
            "Suggestion: add a special character"
        )
        self.assertEqual(check_password("Hello123"), expected)

    # Test Case 3 (a): Invalid Input - Empty Password
    def test_empty_password(self):
        self.assertEqual(check_password(""), "Password cannot be empty.")

    # Test Case 3 (b): Invalid Input - Contains Spaces
    def test_password_with_spaces(self):
        self.assertEqual(check_password("Hello 123"), "Password must not contain spaces.")

    # Test Case 4: Different Valid Scenario (Strong)
    def test_strong_password(self):
        expected = (
            "Strength: Strong (5/5)\n"
            "No suggestions. Your password is secure."
        )
        self.assertEqual(check_password("Hello@123Xy"), expected)


if __name__ == "__main__":
    unittest.main()
