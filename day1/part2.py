input_file = 'adventofcode.com_2025_day_1_input.txt'
dial = 50
ans = 0

with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        clicks = int(line[1:])

        # Full rotations: each 100-click loop hits 0 exactly once
        ans += clicks // 100

        leftover = clicks % 100

        if direction == 'L':
            # Cross 0 during leftover movement (but not if we just land on 0)
            if dial > 0 and leftover -dial > 0:
                ans += 1
            dial = (dial - clicks) % 100

        elif direction == 'R':
            # Cross 0 during leftover movement (but not if we just land on 0)
            if dial > 0 and leftover + dial > 100 :
                ans += 1
            dial = (dial + clicks) % 100

        # Count if we land exactly on 0 at the end of this rotation
        if dial == 0:
            ans += 1

print(ans)
