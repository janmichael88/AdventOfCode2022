from typing import List,Tuple,Iterator,Union
from collections import deque

Grid = List[List[int]]
Pair = Tuple[int,int]


#helper to convert char to int
def char_to_int(char:str) -> int:
    return ord(char) - ord('a')

def parse_input(plain_text:str) -> Tuple[Grid,Pair,Pair]:
    grid = []
    start = None
    end = None

    with open(plain_text) as f:
        lines = [l for l in f.readlines()]
    
    for i,line in enumerate(lines):
        grid.append([])
        for j,char in enumerate(line):
            if char == 'S':
                start = i,j
                char = 'a'
            elif char == 'E':
                end = i,j
                #its supposed to be z here
                char = 'z'
            grid[i].append(char_to_int(char))
    
    assert start is not None
    assert end is not None

    return grid,start,end


#get neighbords function
def get_neighbors(i: int, j: int, nrows: int, ncols: int) -> Iterator[Pair]:
    # left, right, up, down
    neighbors = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]

    for ii, jj in neighbors:
        if 0 <= ii < nrows and 0 <= jj < ncols:
            yield ii, jj


def bfs(grid: Grid, start: Union[List[Pair], Pair], end: Pair):
    nrows, ncols = len(grid), len(grid[0])

    # Queue stores i, j, distance
    # allowed for multiple starts
    if not isinstance(start, list):
        start = [start]

    queue = deque([(s[0], s[1], 0) for s in start])
    seen =  set()

    while queue:
        i, j, distance = queue.popleft()
        if (i, j) == end:
            return distance
        
        for ii, jj in get_neighbors(i, j, nrows, ncols):
            if grid[ii][jj] - grid[i][j] <= 1 and (ii,jj) not in seen:
                
                seen.add((ii, jj))
                queue.append((ii, jj, distance + 1))

#PART 2 IS JUST BFS FROM THE LOWEST POINTS

if __name__ == '__main__':
    grid,start,end = parse_input("input.txt")
    ans = bfs(grid,start,end)
    #find smallest points on grid
    smallest = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                smallest.append((i,j))
    
    ans = float('inf')
    for s in smallest:
        candidate_ans = bfs(grid,s,end)
        if candidate_ans:
            ans = min(candidate_ans,ans)
    
    print(ans)