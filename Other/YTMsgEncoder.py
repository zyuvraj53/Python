sentence = input()

sentence_array = sentence.split(' ')
encoded_sentence_array = []
encoded_character_array = []

for word in sentence_array:
  encoded_sentence_array += [word + '°']
  
encoded_word_sentence = ''.join(encoded_sentence_array)

character_array = list(encoded_word_sentence)

for char in character_array:
  encoded_character_array += [char + '°']
  
encoded_character_sentence = ''.join(encoded_character_array)

size = len(encoded_character_sentence)
# Slice string to remove last 3 characters from string
encoded_character_sentence = encoded_character_sentence[:size - 3]

print(encoded_character_sentence)
