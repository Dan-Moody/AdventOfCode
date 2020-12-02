# answer = 607

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
        minNum = int(passWords[0].split('-')[0])
        maxNum = int(passWords[0].split('-')[1])
        # print ("min: " + str(minNum) + ", max: " + str(maxNum))

        passChar = passWords[1].rstrip(':')

        for ch in passWords[2]:
            if ch == passChar:
                count = count + 1
        
        if count >= minNum and count <= maxNum:
            sum = sum + 1

print(sum)

