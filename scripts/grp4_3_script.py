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

def create_subset_wordlist(input_file, output_file):
    with open(input_file, 'r') as f:
        wordlist = f.read().splitlines()

    subset_wordlist = []
    for word in wordlist:
        if len(word) == 8:
            subset_wordlist.extend(generate_substituted_words(word.capitalize()))

    with open(output_file, 'w') as f:
        f.write('\n'.join(subset_wordlist))

# Usage example
input_file = 'wordlist.txt'  # Replace with your input wordlist file
output_file = 'grp4_3_wordlist.txt'  # Replace with the desired output file name
create_subset_wordlist(input_file, output_file)
