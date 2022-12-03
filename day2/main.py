'''
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
X - Rock
Y - Paper
Z - Scissors
but enemy's version:
A - rock
B - Paper
C - Scissors
PLUS
outcome of the round
DRAW - 3
Loss - 0
WIN - 6

second way is
X -- loss
Y -- Draw
Z -- win
and i need to find out what to pick.
'''
def main():
    points = FirstWayCountPoints(OpenFile('input.txt'))
    print('FIRST WAY')
    print(f'Your enemy scored {points[0]} points. You scored {points[1]}')
    if points[0] > points[1]:
        print('You lost, this elf fooled you.')
    else:
        print('Damn elf didn''t lie about it.')
    pointsv2 = explainedWay(OpenFile('input.txt'))
    print('SECOND WAY')
    print(f'Your enemy scored {pointsv2[0]} points. You scored {pointsv2[1]}')
    if pointsv2[0] > pointsv2[1]:
        print('Oh, that didn''t work. Who would have expected that :v .')
    else:
        print('Sheesh, it works.')
def OpenFile(filename:str):

    with open('input.txt') as f:
        instructions = f.readlines()
        new_list = [item[0:len(item)-1].split() for item in instructions]
        return new_list
def FirstWayCountPoints(instruction:list):
    enemy_score = 0
    my_score = 0
    skillset = [['A','B','C'],['X','Y','Z']]
    winsituations = [['A', 'Y'], ['B', 'Z'], ['C','X']]
    point_matchup = [1,2,3]
    win_indexes = []
    lost_indexes = []
    draw_indexes = []
    for index, item in enumerate(instruction):
        if item in winsituations:
            my_score += 6
            win_indexes.append(index)
        elif skillset[0].index(item[0]) == skillset[1].index(item[1]):
            my_score += 3
            enemy_score += 3
            draw_indexes.append(index)
        elif item not in winsituations:
            enemy_score += 6
            lost_indexes.append(index)
    for index in win_indexes:
        my_score += point_matchup[skillset[1].index(instruction[index][1])]
        enemy_score += point_matchup[skillset[0].index(instruction[index][0])]
    for index in lost_indexes:
        enemy_score += point_matchup[skillset[0].index(instruction[index][0])]
        my_score += point_matchup[skillset[1].index(instruction[index][1])]
    for index in draw_indexes:
        enemy_score += point_matchup[skillset[0].index(instruction[index][0])]
        my_score += point_matchup[skillset[1].index(instruction[index][1])]
    return [enemy_score, my_score]
def explainedWay(instruction:list):
    enemy_score = 0
    my_score = 0
    points = [['A','B','C'],[1,2,3]]
    combinationsv2 = [[['A','B','C'],['C','A','B']],[['A','B','C'],['B','C','A']]]
    for item in instruction:
        if item[1].upper() == 'X':
            my_pick = combinationsv2[0][1][combinationsv2[0][0].index(item[0])]
            my_score += 0 + points[1][points[0].index(my_pick)]
            enemy_score += 6 + points[1][points[0].index(item[0])]
        if item[1].upper() == 'Y':
            my_score += 3 + points[1][points[0].index(item[0])]
            enemy_score += 3 +  points[1][points[0].index(item[0])]
        if item[1].upper() == 'Z':
            my_pick = combinationsv2[1][1][combinationsv2[1][0].index(item[0])]
            my_score += 6 + points[1][points[0].index(my_pick)]
            enemy_score += + 0 + points[1][points[0].index(item[0])]
    return enemy_score, my_score

if __name__ == '__main__':
    main()