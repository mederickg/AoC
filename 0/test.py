def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data


input = get_input(FILE_NAME)

