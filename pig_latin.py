# 026 PIG LATIN
# 7/2/20
#
#########################################

word = input('Please enter any word: ')
first = word[0]
length = len(word)
rest = word[1:length]
if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
    New_Word = word + 'way'
else:
    New_word = rest + first + 'ay'

print(New_word.lower())
