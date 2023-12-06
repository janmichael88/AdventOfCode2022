'''
we are given a list of valves, we can choose to open up a valve
then pressure goes up by 13*number of minutes elapsed
it takes 1 minute to open a valve, or we can chose to not open a valve, in which case
for each valve the we open, we can only for to the next neighboring valves

build hashmap holding flow rates
as well as valves we can go to - dp on subsets
'''
import collections

with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

f.close()

valve_to_rates = collections.defaultdict()
valve_to_neighs = collections.defaultdict(list)
for foo in lines:
    foo = foo.split(" ")
    start_valve = foo[1]
    rate = int(foo[4].split('=')[1].strip(";"))
    #go to point in array where valves
    next_valves = [v.strip(',') for v in foo[9:]]
    valve_to_rates[start_valve] = rate
    for n in next_valves:
        valve_to_neighs[start_valve].append(n)

'''
this is a dp problem
if dp(mins,valve_config) represents the max pressure at mins with valve config
we start with valve AA

this is just dp on subets
state is curr_node, valve config, minutesleft
'''
#need mapper for nodes to interger
get_valve_index = {}
for i,valve in enumerate(sorted(valve_to_rates.keys())):
    get_valve_index[valve] = i

memo = {}

def dp(curr_node,open_valves,minutes):
    if minutes <= 0:
        return 0
    if (curr_node,open_valves,minutes) in memo:
        return memo[(curr_node,open_valves,minutes)]
    #first get node mapping to index
    curr_node_mapping = get_valve_index[curr_node]
    ans = 0
    #if current valve is not open and has a rate
    if not (open_valves & (1 << curr_node_mapping)) and valve_to_rates[curr_node] > 0:
        #get the pressure so far from opening
        curr_pressure = valve_to_rates[curr_node]*(minutes-1)
        #update answer
        ans = max(ans, curr_pressure + dp(curr_node, open_valves | (1 << curr_node_mapping), minutes-1))
    #otherwise we have opteions
    for neigh in valve_to_neighs[curr_node]:
        ans = max(ans,dp(neigh,open_valves,minutes-1))
    
    memo[(curr_node,open_valves,minutes)] = ans
    return ans

temp = dp('AA', 0,30)
print(temp)

'''
for the second part we have 26 minutes but this time we have two players
i time runs out, just return the answer for one less player
if we have 0 players, we have to return 0
'''

memo = {}

def dp2(curr_node,open_valves,minutes,players):
    if players == 0:
        return 0
    if minutes <= 0:
        #go into another dp problem, which was just the first problem with 1 player, and 26 mins
        return dp2('AA',open_valves,26,players-1)
    if (curr_node,open_valves,minutes,players) in memo:
        return memo[(curr_node,open_valves,minutes,players)]
    #first get node mapping to index
    curr_node_mapping = get_valve_index[curr_node]
    ans = 0
    #if current valve is not open and has a rate
    if not (open_valves & (1 << curr_node_mapping)) and valve_to_rates[curr_node] > 0:
        #get the pressure so far from opening
        curr_pressure = valve_to_rates[curr_node]*(minutes-1)
        #update answer
        ans = max(ans, curr_pressure + dp2(curr_node, open_valves | (1 << curr_node_mapping), minutes-1,players))
    #otherwise we have opteions
    for neigh in valve_to_neighs[curr_node]:
        ans = max(ans,dp2(neigh,open_valves,minutes-1,players))
    
    memo[(curr_node,open_valves,minutes,players)] = ans
    return ans

temp = dp2('AA',0,26,2)
print(temp)
