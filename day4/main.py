def main():
    print(OpenFile('input.txt'))
    print(count_overlap(OpenFile('input.txt')))
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
def check_if_overlaps(range1,range2):
    if not range1:
        return True
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

def count_overlap(occurences:list):
    counter = 0
    for i in occurences:
        if check_if_overlaps(range(int(i[0][0]),int(i[0][1])),range(int(i[1][0]),int(i[1][1]))) == True:

            print(i)
            counter += 1
        elif check_if_overlaps(range(int(i[1][0]),int(i[1][1])),range(int(i[0][0]),int(i[0][1]))) == True:
            print(i)
            counter += 1
    return counter

    #return [x.split('-') for x in splitted]


if __name__ == '__main__':
    main()