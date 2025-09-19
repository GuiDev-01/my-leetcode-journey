from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# ------------------------------------------------------------------------------------
# This code block will only be executed when you run the file directly
# using the command: python your_file_name.py
# It's the standard Python entry point for making a script runnable.
# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    # 1. Create an instance of the Solution class to use the twoSum method
    solver = Solution()

    # 2. Define some sample inputs to demonstrate how it works
    print("--- Testing the solution for the Two Sum problem ---")
    
    # Test Case 1
    nums_1 = [2, 7, 11, 15]
    target_1 = 9
    result_1 = solver.twoSum(nums_1, target_1)
    print(f"\nTest Case 1:")
    print(f"Input: nums = {nums_1}, target = {target_1}")
    print(f"Output: {result_1}") # Expected output: [0, 1]

    # Test Case 2
    nums_2 = [3, 2, 4]
    target_2 = 6
    result_2 = solver.twoSum(nums_2, target_2)
    print(f"\nTest Case 2:")
    print(f"Input: nums = {nums_2}, target = {target_2}")
    print(f"Output: {result_2}") # Expected output: [1, 2]
    
    print("\n-------------------------------------------------")