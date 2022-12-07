from collections import defaultdict

def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip().split())
    return data


def build_directory(file):
    path = []
    directories = defaultdict(int)
    for line in file:
        if line[1] == 'cd':
            if line [2] == '/':
                path.append('/')
            elif line[2] == '..':
                path.pop()
            else:
                path.append(line[2])
        elif line[0].isnumeric():
            file_size = int(line[0])
            for i in range(1, len(path)+1):
                directories['/'.join(path[:i])] += file_size
    return(directories)
    
  
def part_one(directories):
    total_size = 0
    for i in directories:
        if directories[i] <= 100000:
            total_size += directories[i]
    print(total_size)
          
def part_two(directories):
    possible_dir = []
    space_availible = 70000000 - directories['/']
    space_needed = 30000000 - space_availible
    for i in directories:
        if directories[i] >= space_needed:
            possible_dir.append([i, directories[i]])
    
    possible_dir.sort(key=lambda x: x[1])
    print(possible_dir[0][1])
    

AoC_input = get_input('7.txt')
dirs = build_directory(AoC_input)

part_one(dirs)
part_two(dirs)
