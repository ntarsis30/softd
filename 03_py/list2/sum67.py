def sum67(nums):
  good,ans = True,0
  for i in nums:
    if i == 6: good = False
    if good: ans+=i
    if i==7: good = True
  return ans
print(sum67([1, 2, 2]))# → 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))# → 5
print(sum67([1, 1, 6, 7, 2]))# → 4