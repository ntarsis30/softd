def sum13(nums):
  ans = 0 if len(nums)==0 else nums[0]*(nums[0]!=13)
  for i in range(1,len(nums)):
    if nums[i]!= 13 and nums[i-1] != 13:
      ans+= nums[i]
  return ans
print(sum13([1, 2, 2, 1]))# → 6
print(sum13([1, 1]))# → 2
print(sum13([1, 2, 2, 1, 13]))# → 6