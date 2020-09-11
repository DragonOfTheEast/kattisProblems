import sys
word_dict = {}
ans = ("false", "true")
for line in sys.stdin.readlines():
    command = line.split()
    if command[0] == "define":
        word_dict[command[2]] = int(command[1])
    elif command[0] == "eval":
            a,b,c = command[1:]
            try:
                if b == "<":
                    print( ans [word_dict[a] < word_dict[c]] )
                elif b == ">":
                    print( ans [word_dict[a] > word_dict[c]] )
                else:
                    print( ans [word_dict[a] == word_dict[c]] )
            except KeyError as e:
                print("undefined")


