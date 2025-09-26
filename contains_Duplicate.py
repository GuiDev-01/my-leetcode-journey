def contains_Duplicate(nums: list) -> bool:
    seen = {}
    
    # For each number in list nums
    for n in nums:
        # Checks if the number it's already in seen
        if n in seen:
            return True
        else:
            seen[n] = n
    return False
            
    
resultado = contains_Duplicate([4,9,8,7,1,7])
print(resultado)