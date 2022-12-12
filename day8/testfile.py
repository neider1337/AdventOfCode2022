#!/usr/bin/python3
import numpy as np


def solve(data):
    ans1 = 0
    ans2 = 0

    # Part 1
    # Determine high points surrounded by only lows in cardinal directions
    for (row, y) in zip(data, range(len(data))):
        data[y] = list(map(int, [*row]))
    print(data)
    data = np.array(data)
    for (x, x_num) in zip(data, range(len(data))):
        for (y, y_num) in zip(x, range(len(x))):
            if (
                    all(data[:x_num, y_num] < y) or  # North
                    all(data[x_num, y_num + 1:] < y) or  # East
                    all(data[x_num + 1:, y_num] < y) or  # South
                    all(data[x_num, :y_num] < y)  # West
            ):
                ans1 += 1

    # Part 2
    # Find tree with highest scenic score (product of visible trees in each direction)\
    scores = []
    for (x, x_num) in zip(data, range(len(data))):
        for (y, y_num) in zip(x, range(len(x))):
            score = 0
            tree_score = 1
            for tree in reversed(data[:x_num, y_num]):  # North
                if y > tree:
                    score += 1
                elif y <= tree:  # When a tree blocks view
                    score += 1
                    break
                else:  # When at the edge
                    break
            tree_score *= score

            score = 0
            for tree in data[x_num, y_num + 1:]:  # East
                if y > tree:
                    score += 1
                elif y <= tree:
                    score += 1
                    break
                else:
                    break
            tree_score *= score

            score = 0
            for tree in data[x_num + 1:, y_num]:  # South
                if y > tree:
                    score += 1
                elif y <= tree:
                    score += 1
                    break
                else:
                    break
            tree_score *= score

            score = 0
            for tree in reversed(data[x_num, :y_num]):  # West
                if y > tree:
                    score += 1
                elif y <= tree:
                    score += 1
                    break
                else:
                    break
            tree_score *= score
            scores.append(tree_score)

    ans2 = max(scores)

    return ans1, ans2


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.read().splitlines()

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")
