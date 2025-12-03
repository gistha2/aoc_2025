input_file = 'adventofcode.com_2025_day_3_input.txt'
with open(input_file,'r') as f:
    lines = f.readlines()
    banks = [line.strip() for line in lines]

ans = 0
for bank in banks:
    largest_batteries = [0]*12
    largest_batteries_indices = [0]*12
    for i in range(12):
        if i == 0:
            start = 0
        else:
            start = largest_batteries_indices[i-1] + 1

        for j in range(start,len(bank) - (12 - i)+1):
            if int(bank[j]) > int(largest_batteries[i]):
                largest_batteries_indices[i] = j
                largest_batteries[i] = bank[j]

    
    ans += int("".join(largest_batteries)) 
    

print(ans)