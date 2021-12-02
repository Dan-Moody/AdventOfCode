dict = {}
# dict["color"] = "red"
# print(dict)
    
accumulator = 0

# Open input for read
with open("..\input.txt") as f:   
    # Read content of the file opened
    content = f.readlines()
    noRepeat = True
    index = 0
    while(noRepeat):
        if index in dict:
            noRepeat = False
        else:
            command = content[index].strip("\n")
            dict[index] = command
            command = command.split(" ")
            if command[0] == "nop":
                index = index + 1
            elif command[0] == "acc":
                if command[1][0] == "+":
                    accumulator += int(command[1][1:])
                else:
                    accumulator -= int(command[1][1:])
                index += 1
            elif command[0] == "jmp":
                if command[1][0] == "+":
                    index += int(command[1][1:])
                else:
                    index -= int(command[1][1:])
print("Accumulator value on repeat: " + str(accumulator))




