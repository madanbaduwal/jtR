def create_subset_wordlist(input_file, output_file):
    with open(input_file, 'r') as f:
        wordlist = f.read().splitlines()

    subset_wordlist = []

    for word in wordlist:
        # Rule 1: 6-letter word, all lowercase
        if len(word) == 6:
            subset_wordlist.append(word.lower())
        
        # Rule 2: 7-letter word, first letter capitalized
        elif len(word) == 7:
            subset_wordlist.append(word.capitalize())
        
        # Rule 3: 8-10 letters, two substitutions, first letter caps, one additional caps padding
        elif 8 <= len(word) <= 10:
            for i in range(len(word)):
                for j in range(i+1, len(word)):
                    for digit1 in '0123456789':
                        for digit2 in '0123456789':
                            new_word = list(word)
                            new_word[i] = digit1
                            new_word[j] = digit2
                            # First letter capitalized
                            new_word[0] = new_word[0].upper()
                            subset_wordlist.append(''.join(new_word))

    with open(output_file, 'w') as f:
        f.write('\n'.join(subset_wordlist))

# Usage example
input_file = 'wordlist.txt'  # Replace with the path to your input wordlist file
output_file = 'grp4_4_wordlist.txt'  # Replace with the desired output file name
create_subset_wordlist(input_file, output_file)


