# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Carter Lain
# Section:      544
# Assignment:   9.19
# Date:         10/31/2024

def get_valid_letters(puzzle):

    clean_puzzle = puzzle.replace(" ","") # Remove all spaces
    clean_puzzle = clean_puzzle.replace(",","") #Remove all commas
    clean_puzzle = clean_puzzle.replace("|","") #Remove all vert bars
    valid_letter_string = ''
    for i in range(0,len(clean_puzzle)):
      if clean_puzzle[i] not in valid_letter_string:  #Build string without dupe letters
          valid_letter_string += clean_puzzle[i]
          if len(valid_letter_string) == 10: 
              break
    return(valid_letter_string)



def is_valid_guess(valid_letter_string, guess_input):
    guess_compare = ''
    if len(guess_input) <= 10:  
        for i in range(0,len(guess_input)): 
          if (guess_input[i] in valid_letter_string) and (guess_input[i] not in guess_compare):
              guess_compare += guess_input[i]
              
        for i in range(0,len(guess_compare)):
            if guess_compare[i] in valid_letter_string and len(guess_compare) == 10:
                return(True)
                break
            else:
                return(False)
                break
    return(False)


def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == quotient * divisor + remainder:
        return(True)
    else:
        return(False)


  
def make_number(word, user_guess):
    number = ''
    for i in word:
         index = user_guess.rfind(i) 
         if index == -1:
            return 0
         number += str(index)
    return(int(number))


 
def make_numbers(puzzle, user_guess):
    puzzle_split=puzzle.split(',') 
    d_d_split= puzzle_split[1].split('|') 
    divisor = d_d_split[0].strip() 
    dividend = d_d_split[1].strip() 
    quotient = puzzle_split[0].strip() 
    remainder = puzzle_split[-1].strip() 
    my_tuple = (int(make_number(dividend, user_guess)), int(make_number(quotient, user_guess)), int(make_number(divisor, user_guess)), make_number(remainder, user_guess))
    return my_tuple



def main():
    puzzle = ""
    guess_input = ""
    print ()
    puzzle = input('Enter a word arithmetic puzzle: ')
    puzzle = puzzle.upper()
    valid_letter_string=get_valid_letters(puzzle)
    print()
    print_puzzle(puzzle)
    print()
    guess_input = input("Enter your guess, for example ABCDEFGHIJ: ")
    guess_input = guess_input.upper()
    if is_valid_guess(valid_letter_string, guess_input):
        guess_tuple = make_numbers(puzzle, guess_input)
        if check_user_guess(guess_tuple[0], guess_tuple[1], guess_tuple[2], guess_tuple[3]):
            print ("Good job!")
        else:
            print ("Try again!")
    else:
        print ("Your guess should contain exactly 10 unique letters used in the puzzle.")



def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")



# STEP 7 - Finally, in your main code type the following:
    
if __name__ == '__main__':
    main()