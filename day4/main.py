def main():
    OpenFile('input.txt')
    print(count_overlap(OpenFile('input.txt')))
    print(count_overlapv3(OpenFile('input.txt')))
def OpenFile(file:str):
    with open (file) as f:
        txt = f.readlines()
        fixed_txt =[x[0:len(x)-1] for x in txt]
    splitted = [x.split(',') for x in fixed_txt]
    fixed_split = []
    for item in splitted:
        temp = []
        for i in item:
            temp.append(i.split('-'))
        fixed_split.append(temp)
    return fixed_split

def count_overlap(occurences:list):
    counter = 0
    for i in occurences:
        z = set(range(int(i[0][0]), int(i[0][1])+1))
        y = set(range(int(i[1][0]), int(i[1][1])+1))
        if z.issubset(y) == True:
            counter += 1
        elif y.issubset(z) == True:
            counter += 1
    return counter


def count_overlapv3(occurences:list):
    counter = 0
    for i in occurences:
        z = set(range(int(i[0][0]), int(i[0][1])+1))
        y = set(range(int(i[1][0]), int(i[1][1])+1))
        if bool(z & y) == True:
            counter += 1
    return counter

'''
I did misunderstood the solution but i am leavin it in here as it looks cool, might be useful. 

def count_overlap_v2(occurences:list):
    counter = 0
    pairs_only = []
    for item in occurences:
        for pair in item:
            pairs_only.append(pair)

    for index, item in enumerate(pairs_only):
        z = set(range(int(item[0]), int(item[1]) + 1))
        set_list = pairs_only[:index] + pairs_only[index+1:]
        for item_v2 in set_list:
            y = set(range(int(item_v2[0]), int(item_v2[1]) + 1))
            if z.issubset(y) == True:
                counter += 1
            elif y.issubset(z) == True:
                counter += 1
    return counter
'''
if __name__ == '__main__':
    main()