
def part_one(path):
    most = 0
    count = 0
    with open (path, 'r') as f:
        for line in f:
            if len(line.strip()) != 0:
                num = int(line)
                count+=num
            else:
                if count > most:
                    most = count
                count = 0
        print('The answer to part 1 is: ' + str(most))
            
            
def part_two(path):
    count = 0
    top_3 = [0, 0, 0]
    final = 0
    with open (path, 'r') as f:
        for line in f:
            if len(line.strip()) != 0:
                num = int(line)
                count+=num
            else:
                top_3.sort()
                for i in range(len(top_3)):
                    if count > top_3[i]:
                        top_3[i] = count
                        break
                count = 0
        for top in top_3:
            final+=top
        
        print('The answer to part 2 is: ' + str(final))
            
            
                
                
part_one('1.txt')
part_two('1.txt')