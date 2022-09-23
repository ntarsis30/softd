def string_match(a, b):
  return sum([a[i:i+2]==b[i:i+2] for i in range(len(a)-1)])
print(string_match('xxcaazz', 'xxbaaz'))# → 3
print(string_match('abc', 'abc'))# → 2
print(string_match('abc', 'axc'))# → 0