# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Carter Lain
# Section:      544
# Assignment:   8.17
# Date:         10/24/2024

#array that holds all the numbers in a 2d array
numbers = [["000", "0 0", "0 0", "0 0", "000"], [" 1 ", "11 ", " 1 ", " 1 ", "111"], ["222", "  2", "222", "2  ", "222"],
           ["333", "  3", "333", "  3", "333"], ["4 4", "4 4", "444", "  4", "  4"], ["555", "5  ", "555", "  5", "555"],
           ["666", "6  ", "666", "6 6", "666"], ["777", "  7", "  7", "  7", "  7"], ["888", "8 8", "888", "8 8", "888"],
           ["999", "9 9", "999", "  9", "999"]]

#hold AM and PM 
ampm = {0:[" A  M   M", "A A MM MM", "AAA M M M", "A A M   M", "A A M   M"], 1:["PPP M   M", "P P MM MM", "PPP M M M", "P   M   M", "P   M   M"]}

#converts a given time into the specified format, replacing numbers with character as needed
def formatTime(character, hour, minute, format):
    time = ""

    #checks the format
    if(format == 12):

        #sets the AM/PM
        dayHalf = 0 if hour < 12 else 1
        #ensures hour is <= 12
        hour = hour - 12 if hour > 12 else hour
        #checks for edgecase of midnight
        if hour == 0:
            hour = 12
        #builds the output
        for i in range(5):
            mid = " : " if (i == 1 or i == 3) else "   "
            time += ((numbers[hour // 10][i] + " " if hour // 10 > 0 else "") + numbers[hour % 10][i] + mid + numbers[minute // 10][i] + " " + numbers[minute % 10][i] + " " + ampm[dayHalf][i] + "\n")
    else:
        #builds the output
        for i in range(5):
                mid = " : " if (i == 1 or i == 3) else "   "
                time += ((numbers[hour // 10][i] + " " if hour // 10 > 0 else "") + numbers[hour % 10][i] + mid + numbers[minute // 10][i] + " " + numbers[minute % 10][i] + "\n")
    
    #replaces digits with the user given character, if needed
    if(character != ""):
        time = time.replace(str(hour // 10), character)
        time = time.replace(str(hour % 10), character)
        time = time.replace(str(minute // 10), character)
        time = time.replace(str(minute % 10), character)
    
    return time




#takes and validates user input
time = input("Enter the time: ")
clockType = int(input("Choose the clock type (12 or 24): "))
while(True):
    if clockType != 12 and clockType != 24:
        clockType = int(input("Invalid clock type, please try again: "))
    else:
        break

#ensures the given character is valid
prefChar = input("Enter your preferred character: ")
allowedChar = "abcdeghkmnopqrsuvwxyz@$&*="
while(True):
    if not(prefChar in allowedChar and len(prefChar) <= 1):
        prefChar = input("Character not permitted! Try again: ")
    else:
        break


#processes time
tSplit = time.split(":")
tHour = int(tSplit[0])
tMin = int(tSplit[1])

#calls formatTime and prints output
print("\n" + formatTime(prefChar, tHour, tMin, clockType), end='')