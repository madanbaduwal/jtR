import itertools

def generate_substituted_words(word):
    substituted_words = []
    for indices in itertools.combinations(range(len(word)), 2):
        for replacement in itertools.product('0123456789', repeat=2):
            substituted_word = list(word)
            for index, digit in zip(indices, replacement):
                substituted_word[index] = digit
            substituted_words.append(''.join(substituted_word))
    return substituted_words

def generate_wordlist(input_file):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    specials = '!@#$%&*-=+'
    padding = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*-=+'

    wordlist = []
    with open(input_file, 'r') as f:
        for line in f:
            word = line.strip()
            if 8 <= len(word) <= 10:
                for word_chars in itertools.combinations(characters, len(word) - 2):
                    for caps_padding in itertools.combinations(padding, 2):
                        for special in specials:
                            word = ''.join(word_chars)
                            word = word.capitalize() + ''.join(caps_padding) + special
                            wordlist.extend(generate_substituted_words(word))
    return wordlist

def create_subset_wordlist(input_file, output_file):
    wordlist = generate_wordlist(input_file)

    with open(output_file, 'w') as f:
        f.write('\n'.join(wordlist))

# Usage example
input_file = 'wordlist.txt'  # Replace with your input wordlist file
output_file = 'grp4_4_wordlist.txt'  # Replace with the desired output file name
create_subset_wordlist(input_file, output_file)
