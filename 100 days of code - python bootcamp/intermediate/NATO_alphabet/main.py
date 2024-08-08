import pandas

nato_alpha = {row.letter:row.code for (index,row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

input_word = input('Enter a word to translate: ').upper()
coded_word = " ".join([nato_alpha[letter] for letter in input_word])
print(coded_word)
