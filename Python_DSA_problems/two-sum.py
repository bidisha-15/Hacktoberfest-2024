def two_sum(nums, target):
    # Create a dictionary to store the value and its index
    num_to_index = {}
    
    for index, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], index]
        
        # Store the number with its index
        num_to_index[num] = index
    
    # If no solution is found
    return None

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    
    if result:
        print(f"Indices of the two numbers that add up to {target}: {result}")
    else:
        print("No two sum solution found.")
