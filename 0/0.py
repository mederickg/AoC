def part_1(path):
    count = 0
    with open (path, 'r') as f:
        for line in f:
            for char in line:
                if char == '(':
                    count+=1
                else:
                    count-=1
        print(count)
    
    
def part_2(path):
    count = 0
    position = 0
    with open (path, 'r') as f:
        for line in f:
            for char in line:
                if char == '(':
                    count+=1
                else:
                    count-=1
                position+=1
                if count == -1:
                    print(position)
                    

                


part_2('0.txt')