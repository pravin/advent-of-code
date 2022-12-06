import re


def read_input():
    stack = [[] for _ in range(9)]
    instructions = []
    with open("05.txt") as fp:
        lines = fp.readlines()
        for x in range(8):
            for y in range(9):
                if lines[x][y * 4 + 1] != " ":
                    stack[y].insert(0, lines[x][y * 4 + 1])

        for line in lines[10:]:
            matchobj = re.match("move (\d+) from (\d+) to (\d+)", line)
            instructions.append(matchobj.groups())

    return stack, instructions


def part1():
    stack, instructions = read_input()
    for num_boxes, from_stack, to_stack in instructions:
        num_boxes = int(num_boxes)
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        for i in range(num_boxes):
            stack[to_stack].append(stack[from_stack].pop())

    return "".join([x.pop() for x in stack])


def part2():
    stack, instructions = read_input()
    for num_boxes, from_stack, to_stack in instructions:
        num_boxes = int(num_boxes)
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        
        stack[to_stack].extend(stack[from_stack][-num_boxes:])
        stack[from_stack] = stack[from_stack][:len(stack[from_stack]) - num_boxes]
    
    return "".join([x.pop() for x in stack])


if __name__ == "__main__":
    print(part1())
    print(part2())
