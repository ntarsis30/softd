def has22(nums):
  for i in range(len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True
  return False
print(has22([1, 2, 2]))# → True
print(has22([1, 2, 1, 2]))# → False
print(has22([2, 1, 2]))# → False