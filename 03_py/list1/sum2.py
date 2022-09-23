def sum2(nums):
  return sum(nums[:min(len(nums),2)])
print(sum2([1, 2, 3]))# → 3
print(sum2([1, 1]))# → 2
print(sum2([1, 1, 1, 1]))# → 2