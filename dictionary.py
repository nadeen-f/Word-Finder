# Returns an array of length 26 where each element is the number of letters 
#   in word that correspond to the index
# ie alpha_letters[0] = 2 means that the word contains 2 of the letter 'a'
def count_letters (word): 
    alpha_letters = [0] * 26
    if (word.isalpha()):
        for letter in word:
            alpha_letters[ord(letter) - ord('a')] += 1
    return alpha_letters

# Returns true if all the letters in dict_word are contained in usr_letters,
#   and otherwise returns false
def compare_letters(usr_letters, dict_word):
    for i in range(26):
        if usr_letters[i] < dict_word[i]:
            return False
    return True

# generates a list of all the words that can be created from a given set of 
#   letters
def check_valid_words(letters):
    valid_words = list()
    usr_letters = count_letters(letters)
    for word in dictionary.keys():
        if (compare_letters(usr_letters, dictionary.get(word))):
            valid_words.append(word)
    return valid_words

f = open("words.txt")
word_list = f.read().split()
dictionary = {word.lower(): count_letters(word.lower()) for word in word_list 
              if len(word) > 2}
f.close()