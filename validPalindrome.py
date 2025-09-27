from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_string = ""
        for char in s:
            if char.isalnum():
                clear_string += char.lower()
        return clear_string == clear_string[::-1]

if __name__ == '__main__':
    solver = Solution()

    print("--- Testing your solution for the Valid Palindrome problem ---")

    # Test Case 1: A classic palindrome
    test_1_input = "A man, a plan, a canal: Panama"
    test_1_result = solver.isPalindrome(test_1_input)
    print(f"\nTest Case 1:")
    print(f"Input: s = \"{test_1_input}\"")
    print(f"Output: {test_1_result}")
    print(f"Expected: True")

    # Test Case 2: A non-palindrome
    test_2_input = "race a car"
    test_2_result = solver.isPalindrome(test_2_input)
    print(f"\nTest Case 2:")
    print(f"Input: s = \"{test_2_input}\"")
    print(f"Output: {test_2_result}")
    print(f"Expected: False")

    # Test Case 3: An empty string (which is a valid palindrome)
    test_3_input = " "
    test_3_result = solver.isPalindrome(test_3_input)
    print(f"\nTest Case 3:")
    print(f"Input: s = \"{test_3_input}\"")
    print(f"Output: {test_3_result}")
    print(f"Expected: True")

    print("\n-------------------------------------------------")
