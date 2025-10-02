from typing import List
class Solution:
    def reverseString(self, s: List) -> None:
        p1 = 0 
        p2 = len(s) - 1
        
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1 
            p2 -= 1 
        
# ------------------------------------------------------------------------------------
# This block of code will only be executed when you run the file directly.
# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    solver = Solution()

    print("--- Testing the solution for the Reverse String problem ---")

    # Test Case 1: Odd number of characters
    test_1_input = ["h", "e", "l", "l", "o"]
    print(f"\nTest Case 1:")
    print(f"Input: s = {test_1_input}")
    solver.reverseString(test_1_input) # This function modifies the list in-place
    print(f"Output: {test_1_input}")
    print(f"Expected: ['o', 'l', 'l', 'e', 'h']")

    # Test Case 2: Even number of characters
    test_2_input = ["H", "a", "n", "n", "a", "h"]
    print(f"\nTest Case 2:")
    print(f"Input: s = {test_2_input}")
    solver.reverseString(test_2_input)
    print(f"Output: {test_2_input}")
    print(f"Expected: ['h', 'a', 'n', 'n', 'a', 'H']")
    
    print("\n-------------------------------------------------") 