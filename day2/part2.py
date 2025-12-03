input_file = 'adventofcode.com_2025_day_2_input.txt'
with open(input_file,'r') as f:
    line = f.readline()

raw_ranges = line.strip().split(',')
ranges = [] 
for raw_range in raw_ranges:
    parts = raw_range.split('-')
    ranges.append([int(part) for part in parts])

ans = 0
#Brute force
for start,end in ranges:
    for num in range(start,end+1):
        str_num = str(num)
        L = len(str_num)
        possible_block_lengths = []
        for B in range(1, L // 2 + 1): # B must be <= L/2 for R >= 2
            if L % B == 0:
                possible_block_lengths.append(B)
                
        for block_length in possible_block_lengths:
            # Split the number string into parts of length 'block_length'
            parts = [str_num[i:i+block_length] for i in range(0, L, block_length)]
            
            # The condition for invalid ID: all parts are the same (repetition)
            if len(set(parts)) == 1:
                ans += num 
                break # Found one pattern, add number and move to the next
        
print(ans)