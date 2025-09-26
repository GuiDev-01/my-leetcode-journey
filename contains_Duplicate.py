from typing import List

# Sua solução, agora dentro da estrutura de classe do LeetCode.
class Solution:
    def containsDuplicate(self, nums: List) -> bool:
        seen = {}
        
        # For each number in list nums
        for n in nums:
            # Checks if the number it's already in seen
            if n in seen:
                return True
            else:
                seen[n] = n
        return False

if __name__ == '__main__':
    # 1. Create an instance of the Solution class
    solver = Solution()

    # 2. Define some test cases to demonstrate your function
    print("--- Testing your solution for the Contains Duplicate problem ---")
    
    # Test Case 1: Should return True
    nums_1 = [1, 2, 7, 4, 5, 7]
    result_1 = solver.containsDuplicate(nums_1)
    print(f"\nTest Case 1:")
    print(f"Input: nums = {nums_1}")
    print(f"Output: {result_1}")
    print(f"Expected: True")

    # Test Case 2: Should return False
    nums_2 = [1, 2, 3, 4]
    result_2 = solver.containsDuplicate(nums_2)
    print(f"\nTest Case 2:")
    print(f"Input: nums = {nums_2}")
    print(f"Output: {result_2}")
    print(f"Expected: False")
    
    print("\n-------------------------------------------------")