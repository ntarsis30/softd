def string_bits(str):
  ans = ""
  for i in range(0,len(str),2):
    ans+=str[i]
  return ans
print(string_bits('Hello'))# → 'Hlo'
print(string_bits('Hi'))# → 'H'
print(string_bits('Heeololeo'))# → 'Hello'