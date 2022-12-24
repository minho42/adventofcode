from pprint import pprint
from utils import read_input

lines = read_input("07.in")


class Node:
    def __init__(self, type, path, size=0, parent=None):
        self.type = type
        self.path = path
        self.size = size
        self.parent = parent

    def __repr__(self):
        return f"{self.path} ({self.type}, {self.size})"


class FS:
    def __init__(self):
        self.cwd = "/"
        self.nodes = [Node(type="dir", path="/", size=0, parent=None)]

    def move(self, dest):
        if self.cwd == dest:
            return

        if dest == "..":
            self.cwd = self.cwd.rpartition("/")[0] or "/"
            return

        self.cwd = (self.cwd + "/" + dest).replace("//", "/")

    def ls(self):
        self.nodes.sort()
        pprint(self.nodes)

    def find(self, path):
        for node in self.nodes:
            if node.path == path:
                return node

    def exist(self, path):
        return self.find(path) is not None

    def add(self, line):
        if not line:
            return

        name = line.split()[-1]
        path = (self.cwd + "/" + name).replace("//", "/")
        parent = self.find(path=self.cwd)

        if line.split()[0] == "dir":
            type = "dir"
            size = 0
        else:
            type = "file"
            size = int(line.split()[0])

        if not self.exist(self.cwd + name):
            node = Node(type=type, path=path, size=size, parent=parent)

            if type == "file":
                mom = node.parent
                while True:
                    try:
                        mom.size += size
                        mom = mom.parent
                    except AttributeError:
                        break

            self.nodes.append(node)


fs = FS()

for line in lines:
    if "$ cd" in line:
        dest = line.split()[-1]
        fs.move(dest)
    elif "$ ls" in line:
        continue
    else:
        fs.add(line)

# fs.ls()


def p1():
    dir_sizes = []

    for node in fs.nodes:
        if node.type == "dir":
            if node.size <= 100000:
                dir_sizes.append(node.size)

    print(sum(dir_sizes))


def p2():
    dir_sizes = []

    for node in fs.nodes:
        if node.type == "dir":
            dir_sizes.append(node.size)

    dir_sizes.sort()
    root_size = dir_sizes[-1]
    total_space = 70000000
    required_space = 30000000
    space_to_free = required_space - (total_space - root_size)

    dirs_to_delete = []

    for s in dir_sizes:
        if s >= space_to_free:
            dirs_to_delete.append(s)
    dirs_to_delete.sort()
    print(dirs_to_delete[0])


p1()
p2()
