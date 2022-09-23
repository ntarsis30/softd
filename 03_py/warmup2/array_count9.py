def array_count9(nums):
  ans = 0
  for i in nums:
    ans+= i == 9
  return ans
print(array_count9([1, 2, 9]))# → 1
print(array_count9([1, 9, 9]))# → 2
print(array_count9([1, 9, 9, 3, 9]))# → 3