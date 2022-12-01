from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

data = puzzle.input_data

elves = data.split('\n\n')

elf_totals = sorted([sum([int(food) for food in elf.split('\n')]) for elf in elves])

solution_part_1 = elf_totals[-1]

print(solution_part_1)

solution_part_2 = sum(elf_totals[-3:])

print(solution_part_2)