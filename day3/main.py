from collections import Counter
import string

def main():
    LookForSimiliarity(OpenFile('input.txt'))
    LookForSimiliarityInGroups(OpenFilev2('input.txt'))

def OpenFile(file:str):
    with open (file) as f:
        txt = f.readlines()
        fixed_txt =[x[0:len(x)-1] for x in txt]
        cut_in_half = []
        for item in fixed_txt:
            cut_item = [item[0:(int(len(item)/2))], item[(int(len(item)/2)):len(item)]]
            cut_in_half.append(cut_item)
        return cut_in_half

def OpenFilev2(file:str):
    with open (file) as f:
        txt = f.readlines()
        fixed_txt =[x[0:len(x)-1] for x in txt]
        return fixed_txt

def LookForSimiliarity(compare_list:list):
    matched_values = []
    for index, item in enumerate(compare_list):
        c1 = Counter(str(item[0]))
        c2 = Counter(str(item[1]))
        R1 = c1 & c2
        matched_values.append([list(i) for i in R1.items()])
    lowercase_ranking = list(string.ascii_lowercase)
    uppercase_ranking = list(string.ascii_uppercase)
    numbers = [list(range(1,27)),list(range(27,53))]
    total_points = 0
    for item in matched_values:
        if lowercase_ranking.count(item[0][0]) != 0:
            total_points += numbers[0][lowercase_ranking.index(item[0][0])]
        elif uppercase_ranking.count(item[0][0]) != 0:
            total_points += numbers[1][uppercase_ranking.index(item[0][0])]
    print(f'Total points granted at first attempt : {total_points}')

    return total_points

def LookForSimiliarityInGroups(compare_list:list):
    three_elves_group = [compare_list[i:i + 3] for i in range(0, len(compare_list), 3)]
    matched_values = []
    for group in three_elves_group:
        C1 = Counter(str(group[0]))
        C2 = Counter(str(group[1]))
        C3 = Counter(str(group[2]))
        R1 = C1 & C2
        R2 = R1 & C3
        matched_values.append([list(i) for i in R2.items()])

    lowercase_ranking = list(string.ascii_lowercase)
    uppercase_ranking = list(string.ascii_uppercase)
    numbers = [list(range(1, 27)), list(range(27, 53))]
    total_points = 0
    for item in matched_values:
        if lowercase_ranking.count(item[0][0]) != 0:
            total_points += numbers[0][lowercase_ranking.index(item[0][0])]
        elif uppercase_ranking.count(item[0][0]) != 0:
            total_points += numbers[1][uppercase_ranking.index(item[0][0])]
    print(f'Total points granted at second attempt : {total_points}')
    return total_points

if __name__ == '__main__':
    main()