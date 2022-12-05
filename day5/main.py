from collections import deque
def main():
    OpenFile('input.txt')
    MoveFieldsListsWay(OpenFile('input.txt'))
    MoveFieldsListsWayMultiple(OpenFile('input.txt'))

'''
                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
 1   2   3   4   5   6   7   8   9 
'''
def OpenFile(input):
    with open(input) as f:
        text = f.readlines()
        text_fixed = [x[0:len(x)-1].split() for x in text]
    return text_fixed

def MoveFieldsListsWay(commands):
    string = ''
    containers = [['S','P','W','N','J','Z'],['T','S','G'],['H','L','R','Q','V'],['D','T','S','V'],['J','M','B','D','T','Z','Q'],['L','Z','C','D','J','T','W','M'],['J','T','G','W','M','P','L'],['H','Q','F','B','T','M','G','N'],['W','Q','B','P','C','G','D','R']]
    for command in commands:
        list_of_moved_containers = containers[int(command[3])-1][0:int(command[1])]
        number_of_container_dest = int(command[5])-1
        number_of_container_source = int(command[3])-1
        amount_of_containers = int(command[1])
        for container in list_of_moved_containers:
            containers[number_of_container_dest].insert(0, container)
        containers[number_of_container_source] = containers[number_of_container_source][amount_of_containers:]
    for i in containers:
        string += i[0]
    return string


def MoveFieldsListsWayMultiple(commands):
    string = ''
    containers = [['S','P','W','N','J','Z'],['T','S','G'],['H','L','R','Q','V'],['D','T','S','V'],['J','M','B','D','T','Z','Q'],['L','Z','C','D','J','T','W','M'],['J','T','G','W','M','P','L'],['H','Q','F','B','T','M','G','N'],['W','Q','B','P','C','G','D','R']]
    for command in commands:
        list_of_moved_containers = containers[int(command[3])-1][0:int(command[1])]
        number_of_container_dest = int(command[5])-1
        number_of_container_source = int(command[3])-1
        amount_of_containers = int(command[1])
        containers[number_of_container_dest] = list_of_moved_containers + containers[number_of_container_dest]
        containers[number_of_container_source] = containers[number_of_container_source][amount_of_containers:]
    for i in containers:
        string += i[0]
    print(string)
    return string
if __name__ == '__main__':
    main()