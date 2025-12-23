def findMedianOptimized(nums1, nums2):
    """
    Optimized approach using binary search on the smaller array
    
    Time Complexity: O(log(min(m, n))) where m and n are lengths of input arrays
    Space Complexity: O(1) - only uses constant extra space
    
    Algorithm:
    1. Apply binary search on the smaller array
    2. Find correct partition point that divides both arrays
    3. Calculate median based on elements around partition
    
    Key Insight:
    - Partition both arrays such that:
      * Left partition has (m+n+1)//2 elements
      * max(left) <= min(right) for valid partition
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
    
    Returns:
        float: The median of combined arrays
    """
    # Ensure nums1 is the smaller array for optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        # Partition nums1 at partitionX
        partitionX = (low + high) // 2
        
        # Partition nums2 such that left side has (m+n+1)//2 elements
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Handle edge cases when partition is at the boundary
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we found the correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Correct partition found
            if (m + n) % 2 == 1:
                # Odd total length: median is max of left partition
                return float(max(maxLeftX, maxLeftY))
            else:
                # Even total length: median is average of max(left) and min(right)
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
        
        elif maxLeftX > minRightY:
            # We are too far right in nums1, move left
            high = partitionX - 1
        else:
            # We are too far left in nums1, move right
            low = partitionX + 1
    
    # Should never reach here if inputs are valid sorted arrays
    raise ValueError("Input arrays are not properly sorted")


# Test cases
if __name__ == "__main__":
    print("Testing Optimized Algorithm:")
    print("=" * 50)
    
    # Test 1
    nums1 = [1, 3]
    nums2 = [2]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 1: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 2.0)")
    print()
    
    # Test 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 2: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 2.5)")
    print()
    
    # Test 3
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 3: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 0.0)")
    print()
    
    # Test 4: Different sizes
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 4: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 4.5)")
    print()
    
    # Test 5: One empty array
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 5: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 3.0)")
    print()
    
    # Test 6: Large arrays
    nums1 = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
    nums2 = list(range(1, 1000, 2))  # [1, 3, 5, ..., 999]
    result = findMedianOptimized(nums1, nums2)
    print(f"Test 6: Large arrays with 1000 elements total")
    print(f"Result: {result} (Expected: 499.5)")
