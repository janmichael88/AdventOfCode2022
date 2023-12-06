#this is just a BFS problem
#starting at the upper left, make your to E
from collections import deque

lines = []
with open("input.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

f.close()

start = [0,0]
end = [0,0]

#conver to list of lists
for i in range(len(lines)):
    lines[i] = list(lines[i])

rows = len(lines)
cols = len(lines[0])

for i in range(rows):
    for j in range(cols):
        if lines[i][j] == 'S':
            start = [i,j]
        if lines[i][j] == 'E':
            end = [i,j]

seen = set()
dirrs = [(1,0),(-1,0),(0,1),(0,-1)]
#into dequre stor as curr_char,letter, and steps
q = deque([('a',start,0)])
seen.add(tuple(start))

while q:
    curr_char, curr_cell, curr_steps = q.popleft()
    if curr_cell == end:
        print(curr_steps)
        
    curr_i = curr_cell[0]
    curr_j = curr_cell[1]
    for dx,dy in dirrs:
        neigh_x = curr_i + dx
        neigh_y = curr_j + dy
        #bounds
        if 0 <= neigh_x < rows and 0 <= neigh_y < cols:
            #not seen
            if (neigh_x,neigh_y) not in seen:
                #can go in that direction
                if ord(lines[neigh_x][neigh_y]) - ord(lines[curr_i][curr_j]) <= 1:
                    seen.add((neigh_x,neigh_y))
                    q.append((lines[neigh_x][neigh_y],[neigh_x,neigh_y],curr_steps+1))


