# answer = 9507
# setting a list equal to another is pass by reference. Use .copy()

# Sum for the 2 sum problem
sum = 0

target = 19690720

# Move each input number into an array and close the input stream once finished
with open(".\input2.txt") as f:   
    # Read each line 
    code = f.readline().split(',')
    codeReset = code.copy()
    noun = 0
    verb = 0
    for noun in range(0, 100):
        code[1] = noun
        for verb in range(0, 100):
            code[1] = noun
            code[2] = verb
            i = 0

            # Computes the output
            while True:
                start = int(code[int(code[i+1])])
                end = int(code[int(code[i+2])])
                if int(code[i]) == 1: # opcode addition
                    code[int(code[i+3])] = start + end
                    i = i + 4
                elif int(code[i]) == 2: # opcode multiplication
                    code[int(code[i+3])] = start * end
                    i = i + 4
                elif int(code[i]) == 99: # opcode exit
                    # print("Exit Success")
                    # print("noun: " + str(code[1]) + " verb: " + str(code[2]))
                    break
                else: #opcode error
                    # print("Exit Failure: " + str(i) + ", code: " + str(code[i]))
                    break

            # Checks if the output equals the target value
            if int(code[0]) == target:
                print("Target aquired: " + str(code[0]))
                print("noun: " + str(code[1]) + " verb: " + str(code[2]))
                break
            code = codeReset.copy()
