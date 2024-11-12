# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 7.18
# Date:         11/7/2024

# create list of consonants and vowels to reference later
consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z')
vowels = ('a','e','i','o','u','y')

phrase = input('Enter word(s) to convert to Pig Latin: ')

# split the phrase to seperate words in string
split_phrase = phrase.split(' ')

piglatin_phrase = []

# function to find the first vowel in the word
def find_first_vowel(word):
    for index, letter in enumerate(word):
        if letter.lower() in vowels:
            return index
    return -1

# for loop to evaluate each word in split_phrase list and convert to piglatin
for word in split_phrase:
    first_vowel_index = find_first_vowel(word)
    if first_vowel_index > 0:
        piglatin = word[first_vowel_index:] + word[:first_vowel_index] + 'ay'
    else:
        piglatin = word + 'yay'
    piglatin_phrase.append(piglatin)

print(f'In Pig Latin, "{phrase}" is: {" ".join(piglatin_phrase)}')