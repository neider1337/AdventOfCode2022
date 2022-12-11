#check why this doesn't work, why it gives too much of output




def main():
    input = process_input('input.txt')
    horizontal_count = process_treelines(input)
    vertical_input = get_vertical_data(input)
    vertical_count = process_treelines(vertical_input)
    print(f'total sum of trees visible is : {horizontal_count + vertical_count}')
def process_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_vertical_data(input):
    vertical_trees = []
    for x in range(len(input)):
        treeline = ''
        for item in input:
            treeline += item[x]
        vertical_trees.append(treeline)
    return vertical_trees

def process_treelines(input):
    counter = 0
    for item in input:
        counter += process_one_treeline(item, False)
        counter += process_one_treeline(item, True)
    return counter

def process_one_treeline(line, reverse):
    tree_counter = 0
    tree_line = []
    if reverse == True:
        one_treeline = line[::-1]
    elif reverse == False:
        one_treeline = str(line)
    else:
        raise Exception('bruh insert reverse value!')
    for index, item in enumerate(one_treeline):
        for tree in item:
            if index == 0:
                tree_counter += 1
                tree_line.append(int(tree))
            elif all(i < int(tree) for i in tree_line) == True:
                tree_counter += 1
                tree_line.append(int(tree))
            else:
                tree_line.append(int(tree))
    return tree_counter

if __name__ == "__main__":
    main()
