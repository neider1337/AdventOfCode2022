import json


def main():
    input = process_input('input.txt')
    filesystem = process_cmd(input)
    dir_sum = 0
    total_disk_space = 70000000
    used_space = filesystem[0]['total_size']
    unused_space = total_disk_space - used_space
    required_unused = 30000000
    space_to_free = required_unused - unused_space
    best_delete_size = total_disk_space
    delete_dir = ''

    dir_items_over300k = []
    for dir_inode, dir in enumerate(filesystem):
        dir_size = dir['total_size']
        if dir_size <= 100000:
            dir_sum += dir_size
        if dir_size >= space_to_free:
            if dir_size < best_delete_size:
                best_delete_size = dir_size
                delete_dir = dir['dir_name']
    print(dir_sum)
    print(best_delete_size)

def process_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()

    input.append('$ EOF')

    return input

def process_cmd(cmds):
    filesystem = []
    cur_dir = -1
    directory = ''
    inode = -1
    for i, cmd_line in enumerate(cmds):
        tkn = cmd_line.split()
        if tkn[0] == '$':
            if directory != '':
                inode += 1
                filesystem.append(directory)
                cur_dir = inode
                directory = ''
            command = tkn[1]
            if command == 'cd':
                argument = tkn[2]
                if argument == '..':
                    cur_dir = filesystem[cur_dir]['parent']
                    dir_name = filesystem[cur_dir]['dir_name']
                else:
                    parent_dir = cur_dir
                    dir_name = argument
            elif command == 'ls':
                directory = {'dir_name':dir_name, 'parent' :parent_dir, 'files':[],'dirs':[], 'total_size':0}
        elif tkn[0] == 'dir':
            subdir = tkn[1]
            directory['dirs'].append(subdir)
        else:
            size = int(tkn[0])
            file = tkn[1]
            directory['files'].append((file, size))
            directory['total_size'] += size

            pdir = directory['parent']
            while True:
                if pdir == -1:break
                filesystem[pdir]['total_size'] += size
                pdir = filesystem[pdir]['parent']

    return filesystem

if __name__ == "__main__":
    main()