input_file = 'adventofcode.com_2025_day_12_input'
regions = []
shapes = []
read_shape = True
shape_idx = 0 
with open(input_file,'r') as f:
    for line in f:
        if 'x' in line:
            read_shape = False
            counts = ([int(val) for val in line.split(':')[1].split()])
            width = int(line.split(':')[0].split('x')[0])
            height = int(line.split(':')[0].split('x')[1])
            regions.append([width,height,counts])

        if read_shape: 
            if line == '\n':
                shape_idx += 1
            else:
                if shape_idx < len(shapes):
                    shapes[shape_idx] += line.count('#')
                else:
                    shapes.append(line.count('#'))

valid_regions = 0
for region in regions:
    w, h, shape_counts = region
    max_area = w*h 
    area_req = 0
    for idx, count in enumerate(shape_counts):
        area_req += count*shapes[idx]
    
    if area_req <= max_area:
        valid_regions += 1

print(valid_regions)
        