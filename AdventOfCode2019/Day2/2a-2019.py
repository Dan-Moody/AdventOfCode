# answer = 3382284

sum = 0

# Move each input number into an array and close the input stream once finished
with open(".\input2.txt") as f:   
    # Read each line 
    code = f.readline().split(',')
    # print(code)
    i = 0
    while True:
        start = int(code[int(code[i+1])])
        end = int(code[int(code[i+2])])
        if int(code[i]) == 1:
            code[int(code[i+3])] = start + end
            i = i + 4
        elif int(code[i]) == 2:
            code[int(code[i+3])] = start * end
            i = i + 4
        elif int(code[i]) == 99:
            print("Exit Success")
            break
        else:
            print("Exit Failure")
            break


print(code)