import sys
word_dict = {}
num_dict = {}
for line in sys.stdin.readlines():
    command = line.split()
    if command[0] == "def":
        if command[1] in word_dict:
            num_dict.pop(word_dict[command[1]])
            word_dict[command[1]] = int(command[2])
            num_dict[int(command[2])] = command[1]
        else:
            word_dict[command[1]] = int(command[2])
            num_dict[int(command[2])] = command[1]
    elif command[0] == "calc":
        done_early = False
        stack = []
        for i in command[1:]:
            if i == '=':
                break
            if i not in word_dict and i != '-' and i != '+':
                done_early = True
                break

            if i != '-' and i != '+':
                stack.append(word_dict[i])
            else:
                op = i

            if len(stack) == 2:
                if op == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
        if done_early is True or stack[0] not in num_dict:
            print(" ".join(command[1:]), "unknown")
        else:
            print(" ".join(command[1:]), num_dict[stack[0]])
    elif command[0] == "clear":
        word_dict.clear()
        num_dict.clear()