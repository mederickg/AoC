# A  X - Rock
# B  Y - Paper
# C  Z - Scissors

# Rock   - 1
# Paper   - 2
# Sissors   - 3
# Loss   - 0
# Tie   - 3
# Win   - 6

play_points = {'X': 1, 'Y': 2, 'Z': 3}

def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

def part_one(file):
    my_score = 0
    for line in file:
        opp_play = line[0]
        my_play = line[2]
        
        my_score += play_points[my_play]
        
        if opp_play == "A":
            if my_play == 'X':
                my_score += 3
            if my_play == "Y":
                my_score += 6
                
        if opp_play == "B":
            if my_play == 'Y':
                my_score += 3
            if my_play == "Z":
                my_score += 6
                
        if opp_play == "C":
            if my_play == 'Z':
                my_score += 3
            if my_play == "X":
                my_score += 6
    print(my_score)
   
   



# A  - Rock -1
# B  - Paper - 2
# C  - Scissors - 3

# X - lose - 0
# Y - draw - 3
# Z - win - 6


def part_two(file):
    my_score = 0
    for line in file:
        opp_play = line[0]
        tie_play = line[2]
        
        if opp_play == "A":
            if tie_play == "X":
                my_score+= 3
            if tie_play == "Y":
                my_score+= 4
            if tie_play == "Z":
                my_score+= 8
            
        if opp_play == "B":
            if tie_play == "X":
                my_score+= 1
            if tie_play == "Y":
                my_score+= 5
            if tie_play == "Z":
                my_score+= 9
            
        if opp_play == "C":
            if tie_play == "X":
                my_score+= 2
            if tie_play == "Y":
                my_score+= 6
            if tie_play == "Z":
                my_score+= 7
    print(my_score)
        







AoC_input = get_input('2.txt')
#print(AoC_input)
part_one(AoC_input)
part_two(AoC_input)