def front_times(str, n):
  return str[:min(len(str),3)]*n
print(front_times('Chocolate', 2))# → 'ChoCho'
print(front_times('Chocolate', 3))# → 'ChoChoCho'
print(front_times('Abc', 3))# → 'AbcAbcAbc'