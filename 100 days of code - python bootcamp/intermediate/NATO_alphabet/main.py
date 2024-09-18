import pandas

nato_alpha = {row.letter:row.code for (index,row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

def generate_phonetic():
    input_word = input('Enter a word to translate: ').upper()

    try:
        coded_word = " ".join([nato_alpha[letter] for letter in input_word])
    except KeyError:
        print('Only letters of the alphabet please.')
        generate_phonetic()
    else:
        print(coded_word)

generate_phonetic()
