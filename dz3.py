word_list=['python', 'c++', 'c', 'scala', 'java']
letter='c'
c_words=[]
def count_letter(word_list, letter):
  for word in word_list:
    if letter in word:
      c_words.append(word)
  print(len(c_words))
  return c_words

print(count_letter(word_list, 'c'))
