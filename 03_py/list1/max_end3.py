def max_end3(nums):
  b = max(nums[0],nums[-1])
  return 3*[b]
print(max_end3([1, 2, 3]))# → [3, 3, 3]
print(max_end3([11, 5, 9]))# → [11, 11, 11]
print(max_end3([2, 11, 3]))# → [3, 3, 3]