from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=4)

data = puzzle.input_data

elf_pairs = data.split('\n')

def check_contains(num_pair1, num_pair2):
    check1 = num_pair1[0] >= num_pair2[0] and num_pair1[1] <= num_pair2[1]
    check2 = num_pair2[0] >= num_pair1[0] and num_pair2[1] <= num_pair1[1]
    return(check1 or check2)

def check_nums(segment):
    halves = segment.split(',')
    ints_ans = [[int(half.split('-')[0]), int(half.split('-')[1])] for half in halves]
    return(check_contains(ints_ans[0], ints_ans[1]))

part1_solution = sum(list(map(check_nums, elf_pairs)))

print(part1_solution)

def check_overlap(num_pair1, num_pair2):
    check1 = max(num_pair1[0], num_pair2[0]) <= min(num_pair1[1], num_pair2[1])
    return(check1)

def check_nums2(segment):
    halves = segment.split(',')
    ints_ans = [[int(half.split('-')[0]), int(half.split('-')[1])] for half in halves]
    return(check_overlap(ints_ans[0], ints_ans[1]))

part2_solution = sum(list(map(check_nums2, elf_pairs)))

print(part2_solution)