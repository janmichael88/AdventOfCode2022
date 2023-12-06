'''
we are given a list of paths
for each path i and i+1 draw a line given the (x,y) positions
sand is pouring in from the points (500,0)
can think of it as a grid of . and #, where # is a rock line and . are air packets
sand is produces one unit at a time
unit of sand falls down one step at a time
if blockes, moves diagonally down and left 
if blocked again, moves down and right
we need to keep pouring a single unit of sand until we can' anymore

it a grain of sand hits boarder of left or right side and can conin
'''


with open ("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

#first build the rock lines
#i need to find the borders of the cave
x_min = float('inf')
x_max = float('-inf')

y_min = float('inf')
y_max = float('-inf')
rock_lines = []
for l in lines:
    l = l.split(' -> ') 
    #each is not [x,y]
    pairs = []
    for p in l:
        x,y = p.split(',')
        x,y = int(y),int(x)
        #find borders
        x_min = min(x_min,x)
        x_max= max(x_max,x)

        y_min = min(y_min,y)
        y_max = max(y_max,y)
        entry = [x,y]
        #entries shold be swapped
        pairs.append(entry)
    rock_lines.append(pairs)

print(x_min,x_max)
print(y_min,y_max)

#make cave
rocks = [['.']*y_max for _ in range(x_max)]

#add in rock lines
for l in rock_lines:
    N = len(l)
    for i in range(N-1):
        first = l[i]
        second = l[i+1]
        #going left to right
        if first[0] == second[0]:
            for j in range(min(first[1],second[1]),max(first[1],second[1])+1):
                rocks[first[0]-1][j-1] = '#'
        #going up to down
        if first[1] == second[1]:
            for j in range(min(first[0],second[0]),max(first[0],second[0])+1):
                rocks[j-1][first[0]-1] = '#'

def move_sand(start):
    #starting at (0,500) try to moved sand uisng rules
    curr_x,curr_y = (0,500)
    #while sand is in bounds
    
