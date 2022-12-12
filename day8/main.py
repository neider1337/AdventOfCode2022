#check why this doesn't work, why it gives too much of output

def main():
    input = process_input('input.txt')
    #horizontal_count = process_treelines(input[0:2])
    vertical_input = get_vertical_data(input)
    #print(input)
    vertical_count = process_treelines(vertical_input)
    print(vertical_count)
    #print(f'total sum of trees visible is : {horizontal_count + vertical_count}')
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
        one_treeline = str(line[::-1])
    elif reverse == False:
        one_treeline = str(line)
    else:
        raise Exception('bruh insert reverse value!')

    print(one_treeline)
    for index, tree in enumerate(one_treeline):
        if index == 0: #if its first tree it always goes into the tree counter
            print(tree)
            tree_counter += 1
            tree_line.append(int(tree))
        elif index != 0 and all(int(i) < int(tree) for i in tree_line) == True: # If all of the trees before the tree are smaller than currently picked tree then add counter
            print(tree)
            print('counter na +')
            tree_counter += 1
            tree_line.append(int(tree))
        else:
            print(tree)
            print('nizsze')
            tree_line.append(int(tree))
    return tree_counter


if __name__ == "__main__":
    main()
