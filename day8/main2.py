#check why this doesn't work, why it gives too much of output
import numpy as np
def main():
    input = process_input('input.txt')
    counter_trees = count_occurences(input)
    print(f'First task : {counter_trees}')
def process_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
        for row, y in zip(input, range(len(input))):
            input[y] = list(map(int, [*row]))
        data = np.array(input)
    return data
def count_occurences(data):
    ans1 = 0
    for (x, x_num) in zip(data, range(len(data))):
        for (y, y_num) in zip(x, range(len(x))):
            if (
                    all(data[:x_num, y_num] < y) or  # North
                    all(data[x_num, y_num + 1:] < y) or  # East
                    all(data[x_num + 1:, y_num] < y) or  # South
                    all(data[x_num, :y_num] < y)  # West
            ):
                ans1 += 1
    return ans1

if __name__ == "__main__":
    main()
