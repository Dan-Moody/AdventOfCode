from ast import Index


dict = {}
# dict["color"] = "red"
# print(dict)
    
accumulator = 0

def cont(acc, i):
    print("todo")


# Open input for read
with open("..\input.txt") as f:   
    # Read content of the file opened
    content = f.readlines()
    noRepeat = True
    index = 0
    while(noRepeat):
        if index in dict or index == len(content):
            noRepeat = False
        else:
            command = content[index].strip("\n")
            print("index: " + str(index) + " cmd: " + command)
            dict[index] = command
            command = command.split(" ")
            if command[0] == "nop":
                cont(accumulator, index)
                index = index + 1
            elif command[0] == "acc":
                if command[1][0] == "+":
                    accumulator += int(command[1][1:])
                else:
                    accumulator -= int(command[1][1:])
                index += 1
            elif command[0] == "jmp":
                cont(accumulator, index)
                if command[1][0] == "+":
                    index += int(command[1][1:])
                else:
                    index -= int(command[1][1:])
        # print(index)
print("Accumulator value on repeat: " + str(accumulator) + " index: " + str(index))




