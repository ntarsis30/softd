def big_diff(nums):
  return max(nums)-min(nums)
print(big_diff([10, 3, 5, 6]))# → 7
print(big_diff([7, 2, 10, 9]))# → 8
print(big_diff([2, 10, 7, 2]))# → 8