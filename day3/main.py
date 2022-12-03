def main():
    OpenFile('input.txt')

def OpenFile(file:str):
    with open (file) as f:
        txt = f.readlines()
        fixed_txt =[x[0:len(x)-1] for x in txt]
        cut_in_half = []

        for item in fixed_txt:
            cut_item = [item[0:(int(len(item)/2))],item[(int(len(item)/2)):len(item)]]
            cut_in_half.append(cut_item)
        print(cut_in_half)
        return cut_in_half
def LookForSimiliarity(compare_list:list):

    return 1


if __name__ == '__main__':
    main()