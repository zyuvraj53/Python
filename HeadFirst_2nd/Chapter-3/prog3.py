vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')

found = {}

for letter in word:
  if letter in vowels:
    found[letter] += 1
    
for k, v in found.items():
  print(k, 'was found', v, 'time(s)')
  
# Raises an error, keys and their values must be initialized

# We can use setdefault()