input_file = 'adventofcode.com_2025_day_5_input.txt'
valid_id_ranges = []
available_ids = []
with open(input_file,'r') as f:
    for line in f:
        line = line.strip()
        if '-' in line:
            valid_id_ranges.append([int(id) for id in line.split('-')])
        elif line.isnumeric():
            available_ids.append(int(line))

#Merge intervals in valid_id_ranges
valid_id_ranges.sort()
merged_id_ranges = []
for valid_id_range in valid_id_ranges:
    if merged_id_ranges and merged_id_ranges[-1][1] >= valid_id_range[0]:
        old_start,old_end = merged_id_ranges.pop()
        merged_id_ranges.append([old_start,max(old_end,valid_id_range[1])])
    else:
        merged_id_ranges.append(valid_id_range)

ans = 0
for id_range in merged_id_ranges:
    ans += id_range[1]-id_range[0]+1
print(ans)
