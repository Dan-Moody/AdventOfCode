# answer = 321

# Sum for the 2 sum problem
sum = 0

# Move each input number into an array and close the input stream once finished
with open(".\input.txt") as f:   
    # Read each line 
    for line in f: 
        count = 0
        # Breaks the string into the 3 important sections and remove trailing newline
        passWords = line.rstrip('\n').split(' ')
        # print(passWords)

        # Read in the password requirements
        posOne = int(passWords[0].split('-')[0])
        posTwo = int(passWords[0].split('-')[1])
        # print ("min: " + str(minNum) + ", max: " + str(maxNum))

        passChar = passWords[1].rstrip(':')

        # Checks to make sure only one of the characters positions matches the desired character
        if (passWords[2][posOne-1] == passChar) != (passWords[2][posTwo-1] == passChar):
            sum = sum + 1
            

print(sum)

