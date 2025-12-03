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
        #Skip odd-length numbers
        str_num = str(num)
        num_len = len(str_num)
        if num_len%2!=0:
            continue
        if str_num[num_len//2:] == str_num[:num_len//2]:
            ans += num

print(ans)