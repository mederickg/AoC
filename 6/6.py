def get_input(path):
    with open(path, 'r') as f:
        data = f.read()
        return(data.strip())

def part_one(file):
    front = 0
    back = 4
    char_count = len(file)
    for i in range(0, char_count):
        if i<= char_count-4:
            arr = []
            for letter in file[front:back]:
                arr.append(letter)
            set_num = set(arr)
            if len(set_num) == 4:
                print(front+4)
                break
            front+=1
            back+=1

def part_two(file):
    front = 0
    back = 14
    char_count = len(file)
    for i in range(0, char_count):
        if i<= char_count-4:
            arr = []
            for letter in file[front:back]:
                arr.append(letter)
            set_num = set(arr)
            if len(set_num) == 14:
                print(front+14)
                break
            front+=1
            back+=1
    


AoC_input = get_input('6.txt')
part_one(AoC_input)
part_two(AoC_input)
