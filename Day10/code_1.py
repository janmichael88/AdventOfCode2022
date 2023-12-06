with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

register = 1
cycles = 0
registers_per_cycle = {}

for l in lines:
    l = l.split()

    #if noop, do nothing but increment cycle by 1
    if l[0] == "noop":
        cycles += 1
        registers_per_cycle[cycles] = register
    
    elif l[0] == "addx":
        for _ in range(2):
            cycles += 1
            registers_per_cycle[cycles] = register
        
        register += int(l[1])

ans = 0
for c in range(20,221,40):
    ans += c*registers_per_cycle[c]

#part 2
pixels = ["."]*40*60

for cycle in range(1,240+1):
    register = registers_per_cycle[cycle]

    #find he position
    pos = (cycle - 1) % 40
    if pos in [register-1,register,register+1]:
        #write pixel to the screen pixel
        #we are now index by cles
        pixels[cycle-1] = "#"

for i in range(0, 201, 40):
	print("".join(pixels[i: i + 40]))