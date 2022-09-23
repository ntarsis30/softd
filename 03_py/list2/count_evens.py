def count_evens(nums):
  ans = 0
  for i in nums:
    ans += i%2 == 0
  return ans
print(count_evens([2, 1, 2, 3, 4]))# → 3
print(count_evens([2, 2, 0]))# → 3
print(count_evens([1, 3, 5]))# → 0