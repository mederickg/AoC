import re

def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data


def part_one(file):
    pattern = '(?P<num1>^\d*)[-](?P<num2>\d*)[,](?P<num3>\d*)[-](?P<num4>\d*)'
    count = 0
    for line in file:
        match = re.search(pattern, line)
        num1, num2, num3, num4 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        
        r1 = set(range(num1, num2+1))
        r2 = set(range(num3, num4+1))

        if r1.issubset(r2):
            count +=1
            pass
        elif r2.issubset(r1):
            count +=1
            pass
    print(count)
    
def part_two(file):
    pattern = '(?P<num1>^\d*)[-](?P<num2>\d*)[,](?P<num3>\d*)[-](?P<num4>\d*)'
    count = 0
    for line in file:
        match = re.search(pattern, line)
        num1, num2, num3, num4 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        
        r1 = set(range(num1, num2+1))
        r2 = set(range(num3, num4+1))

        if len(r1 & r2):
            count+=1
            
    print(count)
    
    
AoC_input = get_input('4.txt')
part_one(AoC_input)
part_two(AoC_input)