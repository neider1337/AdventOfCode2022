def main():
    with open ('input.txt') as f:
        lines = f.readlines()
        top_calories_bag = count_calories(get_items_in_right_order(lines))
        print(top_calories_bag)
        top3 = get_top3_calories(get_items_in_right_order(lines))
        print(top3)


def get_items_in_right_order(lines:list):
    size = len(lines)
    list_comp = []
    idx_list = [idx + 1 for idx, val in
                enumerate(lines) if val == '\n']

    all_calories = [lines[i: j] for i, j in
           zip([0] + idx_list, idx_list +
               ([size] if idx_list[-1] != size else []))]
    for one_cal_list in all_calories:
        temporary_list = list(filter(lambda x : x != '\n' ,one_cal_list))
        temporary_list = [int(item[0:len(item)-1]) for item in temporary_list]
        list_comp.append(temporary_list)
    return list_comp


def count_calories(list_comp:list):
    calories_bag = 0
    for bag in list_comp:
        if sum(bag) > calories_bag:
            calories_bag = sum(bag)
    return calories_bag

def get_top3_calories(list_comp:list):
    sum_list = [sum(bag) for bag in list_comp]
    return sum(sorted(sum_list)[len(sum_list)-3:len(sum_list)])


if __name__ == '__main__':
    main()
