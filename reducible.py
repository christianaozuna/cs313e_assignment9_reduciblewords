"""
Student information for this assignment:

On my/our honor, Christiana Ozuna and Jessica North, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: cmo2388
UT EID 2: jan3557
"""

# the constant used to calculate the step size
STEP_SIZE_CONSTANT = 3


# DO NOT modify this function.
def is_prime(n):
    """
    Determines if a number is prime.

    pre: n is a positive integer.
    post: Returns True if n is prime, otherwise returns False.
    """
    if n == 1:
        return False

    limit = int(n**0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# DO NOT modify this function.
def hash_word(s, size):
    """
    Hashes a lowercase string to an index in a hash table.

    pre: s is a lowercase string, and size is a positive integer representing either
         hash table size or the constant for double hashing.
    post: Returns an integer index in the range [0, size - 1] where the string hashes to.
    """
    hash_idx = 0
    for c in s:
        letter = ord(c) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# WORKS
def step_size(s):
    """
    Calculates step size for double hashing using STEP_SIZE_CONSTANT.

    pre: s is a lowercase string.
    post: Returns the calculated step size as an integer based on the provided string.
    """
    return (STEP_SIZE_CONSTANT - (hash_word(s, STEP_SIZE_CONSTANT) % STEP_SIZE_CONSTANT))


# works
def insert_word(s, hash_table):
    """
    Inserts a string into the hash table using double hashing for collision resolution.
    No duplicates are allowed.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Inserts s into hash_table at the correct index; resolves any collisions
          by double hashing.
    """
    size = len(hash_table)
    string_index = int(hash_word(s, size))
    used_indices = set()

    # if there is a collision
    while hash_table[string_index] is not None:
        # if already in the hash table
        if hash_table[string_index] == s:
            return
        #avoid infinite loop
        if string_index in used_indices:
            raise Exception("Infinite loop detected")
        used_indices.add(string_index)
        # if collision
        string_index = (string_index + step_size(s)) % size
    # inserting
    hash_table[string_index] = s


# works
def find_word(s, hash_table):
    """
    Searches for a string in the hash table.
    Note: using the `in` operator is incorrect as that will be O(N). We want
          an O(1) time average time complexity using hashing.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Returns True if s is found in hash_table, otherwise returns False.
    """
    size = len(hash_table)
    string_index = hash_word(s, size)
    used_indices = set()
    while hash_table[string_index] is not None:
        # if string in hash table
        if hash_table[string_index] == s:
            return True
        # avoid infinite loop
        if string_index in used_indices:
            raise Exception("Infinite loop detected")
        used_indices.add(string_index)
        # if collision, rehash until we find
        string_index = (string_index + step_size(s)) % size
    # not found
    return False

# TODO: Modify this function. You may delete this comment when you are done.
def is_reducible(s, hash_table, hash_memo):
    """
    Determines if a string is reducible using a recursive check.

    pre: s is a lowercase string, hash_table is a list representing the hash table,
         and hash_memo is a list representing the hash table
         for memoization.
    post: Returns True if s is reducible (also updates hash_memo by
          inserting s if reducible), otherwise returns False.
    """
    if s in ["a", "i", "o"]:
        return True
<<<<<<< Updated upstream
    
    # Check if the word is already in the hash_memo
    index = hash_word(s, len(hash_memo))
    if hash_memo[index] == s:
=======
   
    # checking if in cache
    memo_index = hash_word(s, len(hash_memo))
    if hash_memo[memo_index] == s:
>>>>>>> Stashed changes
        return True

    # Check if the word is in the original hash_table
    if not find_word(s, hash_table):
        return False

    # Try removing each letter to form a smaller word
    for i in range(len(s)):
        reduced_word = s[:i] + s[i+1:]
        if is_reducible(reduced_word, hash_table, hash_memo):
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> parent of ef711e2 (reducible failing 2)
            # Store the reducible word in hash_memo
            hash_memo[index] = s
=======
            # adding reduced word to memoization table
            hash_memo[memo_index] = s
>>>>>>> Stashed changes
            return True
    
    return False

# WORKS
def get_longest_words(string_list):
    """
    Finds longest words from a list.

    pre: string_list is a list of lowercase strings.
    post: Returns a list of words in string_list that have the maximum length.
    """
    # finding max length
    max_length = 0
    for string in string_list:
        length = len(string)
        if length > max_length:
            max_length = length

    # finding words with max length
    longest_words = []
    for string in string_list:
        if len(string) == max_length:
            longest_words.append(string)

    return longest_words

import sys
# works? 
def main():
    """The main function that calculates the longest reducible words"""
    # create an empty word_list
    word_list = []
    # read words using input redirection
    for line in sys.stdin.read().splitlines():
        
    # where each line read from input()
    # should be a single word. Append to word_list
    # ensure each word has no trailing white space.
<<<<<<< Updated upstream
        word = line.strip()
        if word:
            word_list.append(word)
    # find length of word_list
    length = len(word_list)
    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_n = is_prime(2 * length)
    # create an empty hash_list  
    # populate the hash_list with N blank strings
    hash_list = [None] * prime_n
=======
    word_list = []
    try:
        while True:
            word = input().strip()
            if word:
                word_list.append(word)
    except EOFError:
        pass

    # find length of word_list
    length_word_list = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    N_minimum = length_word_list * 2
    N = N_minimum + 1
    while not is_prime(N):
        N += 2

    # create an empty hash_list

    # populate the hash_list with N blank strings
    hash_list = [""] * N

>>>>>>> Stashed changes
    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
<<<<<<< Updated upstream
    size_m = is_prime(0.2 * length)
    hash_memo = [None] * size_m
    # populate the hash_memo with M blank strings
    for i in range(size_m):
        hash_memo[i] = None
    # create an empty list reducible_words
    reducible_words = []
=======
    memo_minimum = .2 * len(word_list)
    M = memo_minimum + 1
    while not is_prime(M):
        M += 2

    # populate the hash_memo with M blank strings
    hash_memo = [""] * M

    # create an empty list reducible_words
    reducible_words = []

>>>>>>> Stashed changes
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
<<<<<<< Updated upstream
            if word not in ["a", "i", "o"]:
                insert_word(word, hash_memo)
    # find the largest reducible words in reducible_words
    longest_words = get_longest_words(reducible_words)
    # print the reducible words in alphabetical order
    # one word per line
    longest_words.sort()
    for word in longest_words:
=======

    # find the largest reducible words in reducible_words
    longest_words = get_longest_words(reducible_words)

    # print the reducible words in alphabetical order
    # one word per line
    sorted_longest_words = sorted(longest_words)
    for word in sorted_longest_words:
>>>>>>> Stashed changes
        print(word)

if __name__ == "__main__":
    main()
