def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data





AoC_input = get_input('3.txt')