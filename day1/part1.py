input_file = 'adventofcode.com_2025_day_1_input.txt'
dial = 50
ans = 0
with open(input_file) as f:
    for line in f:
        direction = line[0]
        clicks = int(line[1:])        
        if direction =='L':
            dial = (dial-clicks)%100
        elif direction =='R':
            dial = (dial+clicks)%100
        if dial == 0:
            ans += 1

print(ans) 

