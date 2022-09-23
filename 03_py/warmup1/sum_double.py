def sum_double(a, b):
  return (a+b)*(1+(a==b))
print(sum_double(1, 2))# → 3
print(sum_double(3, 2))# → 5
print(sum_double(2, 2))# → 8
