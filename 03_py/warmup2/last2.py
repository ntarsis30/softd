def last2(str):
  ans = 0
  b = str[len(str)-2:]
  for i in range(len(str)-2):
    ans += str[i:i+2] == b
  return ans

print(last2('hixxhi'))# → 1
print(last2('xaxxaxaxx'))# → 1
print(last2('axxxaaxx'))# → 2