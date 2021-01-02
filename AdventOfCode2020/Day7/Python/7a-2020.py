# answer = 148
# 229

total = 0 # of yes answers

# List of all bags
bags = []

# Look in first bag
initBag = 0

class bag:
    def __init__(self,color,contains):
        self.color = color
        self.contains = contains.copy()
        self.hasGold = False
        self.containsGold()

    def containsGold(self):
        for pack in self.contains:
            # print("packs: " + str(pack))
            if pack[0] != 'no':
                if pack[1] == 'shiny gold':
                    self.reachedGold()
                    # print(self.color)
    
    def hasReachedGold(self):
        return self.hasGold
    
    def reachedGold(self):
        self.hasGold = True
    
# Open input for read
with open(".\input3.txt") as f:   
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

# Search through the bags in bags to see if you get to shiny gold
def dive(sack):
    found = False
    global initBag
    if sack.color == 'shiny gold':
        if initBag != 0:
            return True
    initBag = initBag + 1
    for x in sack.contains: # check if either of the bag objects the sack contains contain shiny gold
        # print("Sack: " + str(sack.color) + " Contains: " + str(x))
        if x[0] != 'no':
            for bog in bags: #Find the bag object for the bag the sack contains 
                # print(sack.color + " innerBag: " + str(x[1]) + str(sack.contains))
                if bog.color == x[1]:
                    # print("sack: " + str(sack.color) + ", bog: " +str(bog.color))
                    if dive(bog):
                        # print(sack.color)
                        found = True
                        sack.reachedGold()
                        # return True
        
    if not found:
        return False
    else: return True

# for sack in bags:
    # print("Sack: " + str(sack.color) + " Contains: " + str(sack.contains) + " Has Gold?: " + str(sack.hasGold))           

for sack in bags:
    # print("Sack: " + str(sack.color) + " Contains: " + str(sack.contains) + " Has Gold?: " + str(sack.hasGold))           
    initBag = 0
    # print(sack.color)
    # if sack.color != 'shiny gold' and dive(sack):
    dive(sack)
        # print("Contains: " + str(sack.contains))
        # total += 1 
print('\n')
for sack in bags:
    print("Sack: " + str(sack.color) + " Contains: " + str(sack.contains) + " Has Gold?: " + str(sack.hasGold))           
    if sack.hasGold:
        total += 1 
print(total)