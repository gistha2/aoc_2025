input_file = 'adventofcode.com_2025_day_3_input.txt'
with open(input_file,'r') as f:
    lines = f.readlines()
    banks = [line.strip() for line in lines]

ans = 0
for bank in banks:
    first_battery = 0
    first_idx = 0

    second_battery = 0
    second_idx = 0
    for i in range(len(bank)-1):
        if int(bank[i]) > first_battery:
            first_idx = i
            first_battery = int(bank[i])
    
    for j in range(first_idx+1,len(bank)):
        if int(bank[j]) > second_battery:
            second_idx = j 
            second_battery = int(bank[j])

    ans += int(str(first_battery)+str(second_battery)) 

print(ans)