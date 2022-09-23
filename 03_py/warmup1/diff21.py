def diff21(n):
  return abs(n-21)*(1+(n>21))

print(diff21(19)) #→ 2
print(diff21(10)) #→ 11
print(diff21(21)) #→ 0
