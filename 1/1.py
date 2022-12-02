
# Open txt file and turn it into an array

def get_input(path):
    with open(path, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data

# add value blocks and adds them to an array
# and sorts by largest value

def make_sorted_list(file):
    count = 0
    arr = []
    for line in file:
        if line != "":
            num = int(line)
            count+=num
        else:
            arr.append(count)
            count = 0   
    arr.sort(reverse=True)
    return(arr)           

# read file and run make_sorted_list to builed a sorted array

AoC_input = get_input('1.txt')
array = make_sorted_list(AoC_input)

# print results

print(array[0])
print(array[0]+array[1]+array[2])
            
                