import sys
data = list()
for line in sys.stdin:
    data.append(line.split())


not_ruler = False

biggest = 0
for i in data:
    list1 = dict()
    for a in range(0, len(i) - 1):
        for b in range(a+1, len(i)):
            change = int(i[b])
            if change > biggest:
                biggest = change
            temp = abs(int(i[a])-int(i[b]))
            if temp not in list1.keys():
                list1[abs(int(i[a])-int(i[b]))] = 1
            else:
                not_ruler = True
                break
        if not_ruler is True:
            break

    if not_ruler is True:
        print("not a ruler")
        not_ruler = False
    elif len(list1) == biggest and not_ruler is False:
        print("perfect")
    elif len(list1) != biggest and not_ruler is False:
        print("missing", end=" ")
        for key in range(1, biggest):
            if key not in list1.keys():
                print(key, end=" ")

    biggest = 0
