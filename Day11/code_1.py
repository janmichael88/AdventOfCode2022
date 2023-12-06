from collections import deque,Counter
'''
this is an OOP question
first we need to make a Monkey API
each monkey can hold items

'''
class Monkey:
    def __init__(self,items,operation,test,first,second):
        self.items = deque(items)
        self.operation = operation
        self.test = test
        self.first = first
        self.second = second

    def check_items(self):
        #decide where monkey passes the item
        old = self.items.popleft()
        #update
        curr_item = eval(self.operation)
        #bored
        curr_item //= 3
        #test
        if curr_item % self.test == 0:
            #return the item level and the next monkey it goes to
            return [curr_item,self.first]
        else:
            return [curr_item,self.second]

#get input and build the monkeys
with open("input.txt") as f:
    lines = [l.strip() for l in f]

#every seven lines is a monkey
monkeys = []
for i in range(0,len(lines),7):
    monk = lines[i:i+7]
    #get the items
    items = [int(foo) for foo in monk[1].split(':')[1].strip().split(",")]
    #for operation we want after the == sign
    op = monk[2].split("=")[-1].strip()
    test = int(monk[3].split(' ')[-1].strip())
    first_monkey = int(monk[4].split(' ')[-1])
    second_monkey = int(monk[5].split(' ')[-1])
    
    #make a monkey
    new_monkey = Monkey(items,op,test,first_monkey,second_monkey)
    monkeys.append(new_monkey)

#we define a round a monkey clearing out all its tiems
#we want to do 20 rounds, and for all 20 rounds count the number of times each monkey inspects
#find the two monst active monkeys and return their product
counts = Counter()
for i in range(20):
    i %= len(monkeys)
    #get the monkey
    curr_monkey = monkeys[i]
    #hold curr count
    curr_count = 0
    while curr_monkey.items:
        new_item,next_monkey = curr_monkey.check_items()
        #add the next item to the monkey
        monkeys[next_monkey].items.append(new_item)
        curr_count += 1
    
    counts[i] += curr_count

print(counts.values())