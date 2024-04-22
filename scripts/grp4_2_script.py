def generate_substituted_words(word):
    substituted_words = []
    for i in range(len(word)):
        if word[i].isalpha():
            for digit in '0123456789':
                substituted_word = word[:i] + digit + word[i+1:]
                substituted_words.append(substituted_word)
    return substituted_words

def create_subset_wordlist(input_file, output_file):
    with open(input_file, 'r') as f:
        wordlist = f.read().splitlines()

    subset_wordlist = []
    for word in wordlist:
        if len(word) == 7:
            subset_wordlist.extend(generate_substituted_words(word))

    with open(output_file, 'w') as f:
        f.write('\n'.join(subset_wordlist))

# Usage example
input_file = 'wordlist.txt'  # Replace with your input wordlist file
output_file = 'grp4_2_wordlist.txt'  # Replace with the desired output file name
create_subset_wordlist(input_file, output_file)
