def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W',
               'X', 'Y', 'Z']

def part_one(file):
    score = 0
    match = []
    for line in file:
        ruck1 = line[:len(line)//2]
        ruck2 = line[len(line)//2:]
        for letter in ruck1:
            if letter in ruck2:
                match.append(letter)
                break
    for item in match:
            score += letter_list.index(item)+1
    print(score)  

match = []

def slide(file, start, end):
    arr = []
    for item in file[start:end+1]:
        arr.append(item)
    ruck1 = arr[0]
    ruck2 = arr[1]
    ruck3 = arr[2]
    
    for letter in ruck1:
        if letter in ruck2 and letter in ruck3:
           match.append(letter) 
           break       
        
def part_two(file):
    start = 0
    end = 2
    score = 0
    for num in range(len(file)//3):
        slide(file, start, end)
        start+=3
        end+=3
        
    for item in match:
            score += letter_list.index(item)+1
    print(score)
    
         



AoC_input = get_input('3.txt')
part_one(AoC_input)
part_two(AoC_input)