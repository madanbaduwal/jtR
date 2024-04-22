def create_subset_wordlist(input_file, output_file):
    with open(input_file, 'r') as f:
        wordlist = f.read().splitlines()

    subset_wordlist = [word.lower() for word in wordlist if len(word) == 6]

    with open(output_file, 'w') as f:
        f.write('\n'.join(subset_wordlist))

# Usage example
input_file = 'wordlist.txt'  # Replace with your input wordlist file
output_file = 'grp4_0_wordlist.txt'  # Replace with the desired output file name
create_subset_wordlist(input_file, output_file)
