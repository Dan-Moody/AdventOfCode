# answer = 148
# 229

total = 0 # of yes answers

# List of all bags
bags = []

# Look in first bag
initBag = 0

# dictionary for no bags
dict = {}

class bag:
    def __init__(self,color,contains):
        self.color = color
        self.contains = contains.copy()
        self.hasGold = False
        self.containsGold()

    def containsGold(self):
        for pack in self.contains:
            # print("packs: " + str(pack))
            if pack[0] == 'no':
                dict[self.color] = ''
                # print(self.color)
    
    def hasReachedGold(self):
        return self.hasGold
    
    def reachedGold(self):
        self.hasGold = True
    
# Open input for read
with open(".\input2.txt") as f:   
    # Read each line
    for line in f:
        line = line.strip("\n")
        line = line.split("contain ")
        color = line[0].rstrip(" bags")
        temp = line[1].rstrip(".").split(", ")
        contains = []
        for x in temp:
            x = x.split()
            # print(x)
            contains.append([x[0],x[1]+" "+x[2]])
        # contains = line[1].split(", ")
        # print(line)
        bags.append(bag(color,contains))
        # print(color)
        # print(contains)

hasChanged = True
inDict = True
while hasChanged:
    hasChanged = False
    for bag in bags:
        if bag.color not in dict:
            inDict = True
            for content in bag.contains: # check if either of the bag objects the sack contains contain shiny gold
                if content[1] not in dict or content[1] == 'shiny gold':
                    inDict = False 
                    break
            if inDict:
                dict[bag.color] = ''
                hasChanged = True

# for x in dict:
#     print(x)
print(len(dict))
print(len(bags) - len(dict))