# Working : print(open('big.txt').read())

import re,string
from collections import Counter

# Tokenize the text
def words(input_text_file = open('big.txt').read()):
    return re.findall(r'\w+',input_text_file.lower())

# Create the frequency count of all words in the dictionary D for prior and likelihood.
WORDS_COUNT = Counter(words(input_text_file = open('big.txt').read()))
# Test : print(WORDS_COUNT)
# Language Model
def lm(word,N = sum(WORDS_COUNT.values())):
    return WORDS_COUNT[word] / N

# Main function
def correct_spelling(word):
    # Return argmax of P(x|w)P(w)
    return max(candidates(word), key=lm)  # Find max based on key probability obtained from the language model function, this makes the function an argmax.

# Candidate set / Error model
def candidates(word):
    ''' Return set of words that iff
    1. They exist in the dictionary
    2. They are at an edit distance of 1
    3. They are at an edit distance of 2
    4. The word itself, even if it's non-existant in the dictionary
    '''
    return (known([word]) or known(edit_distance1(word)) or known(edit_distance2(word)) or [word])

# Function to check if the word in question exists in the dictionary
def known(words):
    return set(word for word in words if word in WORDS_COUNT)

# Find words at an edit distance / Damerau-Levenshtein distance = 1
def edit_distance1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Split the word into (LHS,RHS) combos of constituent characters
    splits = [(word[:i],word[i:]) for i in range(len(word) + 1)]
    # Creating the matrices for the 4 confusion matrices
    '''
    1. Deletion
    2. Transposition
    3. Replacement
    4. Insertion
    '''
    # Logic written for x = 'speling'
    deletes = [L + R[1:] for L,R in splits if R]
    # LOGIC : if ('sp','eling'), then --> L + R[1:] = 'spling'
    transposes = [L + R[1] + R[1] + R[2:] for L,R in splits if len(R) > 1]
    # LOGIC : if ('sp','eling'), then --> L + R[1] + R[1] + R[2:] = 'spleing'
    replaces = [L + c + R[1:] for L,R in splits if R for c in letters]
    # LOGIC : if ('sp','eling'), then --> L + c + R[1:] -->
    '''
    Run 1 --> 'spaling'
    Run 2 --> 'spbling'
    Run 3 --> 'spcling'
    .
    .
    .
    Run 26 --> 'spzling'
    '''
    inserts = [L + c + R for L,R in splits for c in letters]
    # LOGIC : if ('sp','eling'), then --> L + c + R -->
    '''
    Run 1 --> 'spaeling'
    Run 2 --> 'spbeling'
    Run 3 --> 'spceling'
    .
    .
    .
    Run 26 --> 'spzeling'
    '''
    return set(deletes + transposes + replaces + inserts)

# Find words at an edit distance / Damerau-Levenshtein distance = 2
def edit_distance2(word):
    '''
    BASIC LOGIC for edit distance = 2 : Edit distance will be two if we repeat edit_distance1() function
    on all words obtained from the above function (those having edit distance = 1)
    Will provide sample for all 1 case as example :
    
    Say, x = 'speling'
    Let's work on ('sp','eling')
    If we look at deletion :
    edit1 = 'spling'
    Take ('sp','ling')
    edit2 = 'sping'

    If we look at transposition :
    edit1 = 'spleing'
    Take ('spl','eing')
    edit2 = 'splieng'

    If we look at replacement :
    edit1 = 'spaling'
    Take ('spa','ling')
    edit2 = ['spaaling','spabling','spacling',......,'spazling']

    If we look at insertion :
    edit1 = 'spaeling'
    Take ('spa','eling')
    edit2 = ['spaaeling','spabeling','spaceling',......,'spazeling']
    '''
    return (edit2 for edit1 in edit_distance1(word) for edit2 in edit_distance1(edit1))

# Test run
print(correct_spelling('breka'))
