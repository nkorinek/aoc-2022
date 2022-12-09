from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=7)

data = puzzle.input_data

# input = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

input = data

class Folder:
    def __init__(self, name, parent, content=[]):
        self.name = name
        self.parent = parent
        self.content = content
    def add_file(self, file):
        self.content.append(file)
    def get_name(self):
        return self.name
    def get_parent(self):
        return self.parent
    def get_contents(self):
        return self.content
    def print_conents(self):
        for contents in self.content:
            print(contents.get_name())
    def get_size(self):
        size = 0
        for contents in self.content:
            if type(contents) == File:
                size += contents.get_size()
            elif type(contents) == Folder:
                size += contents.get_size()
        return size
    def get_size_list(self, folder_sizes_list):
        size = 0
        for contents in self.content:
            if type(contents) == File:
                size += contents.get_size()
            elif type(contents) == Folder:
                folder_size = contents.get_size()
                folder_name = contents.get_name()
                folder_sizes_list.append([folder_size, folder_name])
                contents.get_size_list(folder_sizes_list)
        return folder_sizes_list

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size

def crawler(line, current_folder):
    commands = line.split(" ")
    print("----{}----".format(current_folder.get_name()))
    current_folder.print_conents()
    if commands[0] == "$":
        if commands[1] == "cd":
            if commands[2] == "..":
                return current_folder.get_parent()
            elif commands[2] == "/":
                while current_folder.get_parent() != "/":
                    current_folder = current_folder.get_parent()
                return current_folder
            else: 
                folder_contents = current_folder.get_contents()
                for contents in folder_contents:
                    if type(contents) == Folder:
                        if contents.get_name() == commands[2]:
                            return contents
        elif commands[1] == "ls":
            return current_folder
    elif commands[0] == "dir":
        folder = Folder(commands[1], current_folder, [])
        current_folder.add_file(folder)
        return current_folder
    else:
        fil = File(commands[1], int(commands[0]))
        current_folder.add_file(fil)
        return current_folder

Home_folder = Folder("/", "/")

folder = Home_folder

for i in input.split('\n'):
    folder = crawler(i, folder)

folder_sizes = Home_folder.get_size_list([])

solution_part_1 = 0

for i in folder_sizes:
    if i[0] <= 100000:
        solution_part_1 += i[0]

print(solution_part_1)

total_space = 70000000

used_space = Home_folder.get_size()

available_space = total_space - used_space

space_needed = 30000000 - available_space

solution_part_2 = 30000000

for i in folder_sizes:
    if i[0] >= space_needed and i[0] <= solution_part_2:
        solution_part_2 = i[0]

print(solution_part_2)