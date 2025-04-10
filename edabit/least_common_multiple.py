from typing import List


# Compute GCD using Euclidean algorithm
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Compute LCM of two numbers
def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


# Compute LCM of a list of numbers
def lcm_list(nums: List[int]) -> int:
    if not nums:
        return 0  # or raise an error, depending on your needs

    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result


# Test cases
print(lcm_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 2520
print(lcm_list([5]))  # 5
print(lcm_list([5, 7, 11]))  # 385
print(lcm_list([5, 7, 11, 35, 55, 77]))  # 385
