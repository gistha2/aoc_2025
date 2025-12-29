from scipy.optimize import linprog
from scipy.optimize import LinearConstraint
import numpy as np
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

        machine = [buttons, joltage] 
        machines.append(machine)

total_presses = 0
for machine in machines:
    state = [0]*len(machine[-1])
    buttons_vectors = machine[:-1][0]
    target_vector = machine[-1]
    buttons_vectors, target_vector = machine
    num_counters = len(target_vector)
    num_buttons = len(buttons_vectors)
    
    # Use scipy to solve equality constraints A.x = b with minimal x (c=num. button presses), see https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
    # Matrix A: rows = counters, columns = buttons for A
    # B = target_vector
    A = np.zeros((num_counters, num_buttons))
    for j, btn_indices in enumerate(buttons_vectors):
        for i in btn_indices:
            A[i, j] = 1
    c = np.ones(num_buttons)

    res = linprog(
        c, 
        A_eq=A, 
        b_eq=target_vector, 
        integrality=1,      # This broadcasts '1' to all variables
        bounds=(0, None)    # Presses must be non-negative
    )

    if res.success:
        total_presses += int(round(res.fun))
       
print(total_presses)