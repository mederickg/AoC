import re

# index 1 = first row
# index 5 = second row
# index 9 = third
#
#
def get_cargo(file):
    with open(file, 'r') as f:
        crates = []
        stacks = 9
        for x in range(0,stacks):
            crates.append([])
        for line in f:
            index = 1
            if line[1] == '1':
                break
            for i in range(0, stacks):
                if line[index] != ' ' and line[index]!= '\n':
                    crates[(index-1)//4].append(line[index])
                index += 4
        for arr in crates:
            arr.reverse()
    return(crates)
            
def read_moves(file):
    crates = get_cargo(file)
    pattern = '^move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)'
    with open(file, 'r') as f:
        for line in f:
            if line[0] == 'm':
                regex= re.search(pattern, line)
                m_amount = int(regex.group(1))
                crate_num = int(regex.group(2))-1
                dest_crate = int(regex.group(3))-1
                print(m_amount, crate_num, dest_crate)
                for i in range(0,m_amount):
                    
                    c = crates[crate_num].pop()
                    print("popped: " + c)
                    crates[dest_crate].append(c)
        print(crates)
        for crate in crates:
            print(crate.pop())

def read_moves_2(file):
    crates = get_cargo(file)
    pattern = '^move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)'
    with open(file, 'r') as f:
        for line in f:
            if line[0] == 'm':
                regex= re.search(pattern, line)
                m_amount = int(regex.group(1))
                crate_num = int(regex.group(2))-1
                dest_crate = int(regex.group(3))-1
                
                removed = crates[crate_num][-m_amount:]
                del crates[crate_num][-m_amount:]
                
                for value in removed:
                    crates[dest_crate].append(value)
                
        for crate in crates:
            print(crate.pop())    



# #read_moves('5.txt')
read_moves_2('5.txt')



 