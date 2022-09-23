def string_splosion(str):
  return "".join([str[:i] for i in range(len(str)+1)])
print(string_splosion('Code'))# → 'CCoCodCode'
print(string_splosion('abc'))# → 'aababc'
print(string_splosion('ab'))# → 'aab'