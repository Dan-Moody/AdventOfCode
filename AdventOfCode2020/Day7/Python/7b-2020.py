# answer = 148
# 229

dict = {}
# dict["color"] = "red"
# print(dict)
    
# Open input for read
with open(".\input.txt") as f:   
    # Read each line
    for line in f:
        line = line.strip("\n")
        line = line.split(" contain ")
        dict[line[0]] = line[1]

count = 0
# Search through a bag and count how many they contain
def search(color):
    global count
    bagContains = dict[color]
    if "no " in bagContains:
        return
    else:
        bags = bagContains.split(", ")
        for bag in bags:
            bag = bag.strip(".")
            # print(bag)
            number = int(bag[0])
            count = count + number
            # print(count)
            nextBag = bag.split(" ", 1)[1]
            if nextBag[-1] != "s":
                nextBag = nextBag + "s"
            for i in range(number):
                search(nextBag)

        # print(bags[0])


# print(dict[])
search("shiny gold bags")
print(count)