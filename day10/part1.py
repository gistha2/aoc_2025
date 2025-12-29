from collections import deque
input_file = 'adventofcode.com_2025_day_10_input.txt'
example_file = 'example.txt'

#Each line represents a machine with: list of indicator_lights, list of  buttons, list of joltage in order
machines = []

with open( input_file,'r') as f:
    for line in f:
        raw_line = line.split()
        indicators = raw_line[0]
        buttons = []
        joltage = []
        #Indicator lights
        indicator_binary = []
        for c in indicators:
            if c == '[' or c==']':
                continue
            elif c == '#':
                indicator_binary.append(True)
            else:
                indicator_binary.append(False)
        #buttons
        for elem in raw_line[1:]:
            if elem[0] == '(':
                buttons.append([int(val) for val in elem.strip('(').strip(')').split(',')])
            elif elem[0] == '{':
                joltage = ([int(val) for val in elem.strip('{').strip('}').split(',')])

        machine = [indicator_binary, buttons, joltage]
        machines.append(machine)

#State = light status e.g. initially [0,0,0,0]
#Transition based on buttons e.g. for button [0]: [0,0,0,0] -> [1,0,0,0]
#Target state e.g. [0,1,1,0]
#Returns depth (number of button presses) to achieve target state
def bfs(target, transitions):
    depth = 0 
    visited = set([])
    #Initalise queue with initial state ([0,0,0,0])
    queue = deque([[False]*len(target)])
    depth = 0
    while queue:
        n_queue = len(queue)
        for _ in range(n_queue):
            state = queue.popleft()
            if tuple(state) in visited:
                continue
            if state == target:
                return depth 
            visited.add(tuple(state))

            for transition in transitions:
                new_state = state.copy()
                for idx in transition:
                    new_state[idx] = not state[idx]         
                queue.append(new_state)
        depth += 1 
    return -1 #Target never found 

ans = 0
for i in range(len(machines)):
    num_presses = bfs(machines[i][0],machines[i][1])
    ans += num_presses

print(ans)