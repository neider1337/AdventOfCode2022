from collections import deque
def main():
    OpenFile('input.txt')
    MoveFields(OpenFile('input.txt'))
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

def MoveFields(commands):
    containers = [['S','P','W','N','J','Z'],['T','S','G'],['H','L','R','Q','V'],['D','T','S','V'],['J','M','B','D','T','Z','Q'],['L','Z','C','D','J','T','W','M'],['J','T','G','W','M','P','L'],['H','Q','F','B','T','M','G','N'],['W','Q','B','P','C','G','D','R']]
    for item in commands:
        print(item)
        what = containers[int(item[3])-1][0:int(item[1])]
        for letter in what:
            containers[int(item[5]) - 1].insert(0 ,letter)
        containers[int(item[3])-1] = containers[int(item[3])-1][int(item[1]):len(containers[int(item[3])-1])]

    return containers

if __name__ == '__main__':
    main()
