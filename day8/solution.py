from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=8)

data = puzzle.input_data

test = """30373
25512
65332
33549
35390"""

input = data

arr_list = []

for i in input.split('\n'):
    arr_list.append(np.fromiter(i, dtype=int))

arr = np.array(arr_list)
x, y = arr.shape

perimeter = 2*x + 2*y - 4

def is_visible(array, x, y):
    tree_height = array[x][y]
    vis_south = array[x+1:,y]
    vis_north = array[:x,y]
    vis_west = array[x,:y]
    vis_east = array[x,y+1:]
    not_visible = []
    directions = [vis_south, vis_north, vis_west, vis_east]
    for dir in directions:
        not_visible.append(np.any(dir>=tree_height))
    return sum(not_visible) != 4

visible_trees = []

for i in range(x):
    if i != 0 and i != x-1:
        for j in range(y):
            if j != 0 and j != y-1:
                visible_trees.append(is_visible(arr, i, j))


solution_part_1 = perimeter + sum(visible_trees)

print(solution_part_1)

def scenic_scorer(array, x, y):
    tree_height = array[x][y]
    vis_south = array[x+1:,y]
    vis_north = np.flip(array[:x,y])
    vis_west = np.flip(array[x,:y])
    vis_east = array[x,y+1:]
    directions = [vis_south, vis_north, vis_west, vis_east]
    scores = []
    for dir in directions:
        score = 0
        for height in dir:
            if height >= tree_height:
                score += 1
                break
            else:
                score += 1
        scores.append(score)
    return np.prod(scores)

tree_scores = []

for i in range(x):
    if i != 0 and i != x-1:
        for j in range(y):
            if j != 0 and j != y-1:
                tree_scores.append(scenic_scorer(arr, i, j))

print(max(tree_scores))

