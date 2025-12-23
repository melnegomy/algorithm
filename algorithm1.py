def findMedianNaive(nums1, nums2):
    """
    Naive approach: Merge both sorted arrays and find median
    
    Time Complexity: O(m + n) where m and n are lengths of input arrays
    Space Complexity: O(m + n) for storing merged array
    
    Algorithm:
    1. Merge two sorted arrays into one sorted array
    2. Find the median by accessing middle element(s)
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
    
    Returns:
        float: The median of combined arrays
    """
    merged = []
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    
    # Merge two sorted arrays
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Append remaining elements from nums1
    while i < m:
        merged.append(nums1[i])
        i += 1
    
    # Append remaining elements from nums2
    while j < n:
        merged.append(nums2[j])
        j += 1
    
    total = len(merged)
    
    # Find median
    if total % 2 == 1:
        # Odd number of elements: return middle element
        return float(merged[total // 2])
    else:
        # Even number of elements: return average of two middle elements
        mid1 = merged[total // 2 - 1]
        mid2 = merged[total // 2]
        return (mid1 + mid2) / 2.0


# Test cases
if __name__ == "__main__":
    print("Testing Naive Algorithm:")
    print("=" * 50)
    
    # Test 1
    nums1 = [1, 3]
    nums2 = [2]
    result = findMedianNaive(nums1, nums2)
    print(f"Test 1: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 2.0)")
    print()
    
    # Test 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = findMedianNaive(nums1, nums2)
    print(f"Test 2: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 2.5)")
    print()
    
    # Test 3
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = findMedianNaive(nums1, nums2)
    print(f"Test 3: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 0.0)")
    print()
    
    # Test 4: Different sizes
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6]
    result = findMedianNaive(nums1, nums2)
    print(f"Test 4: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 4.5)")
    print()
    
    # Test 5: One empty array
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    result = findMedianNaive(nums1, nums2)
    print(f"Test 5: nums1={nums1}, nums2={nums2}")
    print(f"Result: {result} (Expected: 3.0)")