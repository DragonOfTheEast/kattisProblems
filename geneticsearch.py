def _test_string(string, test_string):
   ans = 0
   index = 0
   prev_ans = 0
   while True:
        prev_ans = string[index:].find(test_string)
        if prev_ans == -1:
            break
        ans += 1
        index += prev_ans +1
   return ans
def _test_string_remove_char(string, test_string):
    ans = 0
    seen = set()
    for index, char in enumerate(test_string):
        temp = test_string[:index] + test_string[index+1:]
        if temp in seen:
            continue
        seen.add(temp)
        ans += _test_string(string, temp)
    return ans
def _test_string_add_char(string, test_string):
    seen = set()
    ans = 0
    for char in ['A', 'G', 'T', 'C']:
        for index in range(len(test_string)+1):
            temp = test_string[:index] + char + test_string[index:]
            if temp in seen:
                continue
            seen.add(temp)
            ans += _test_string(string, temp)
    return ans

while True:
    line = input()
    if line == "0":
        break
    test_string, main_string = [i for i in line.split()]
    print(_test_string(main_string, test_string), _test_string_remove_char(main_string, test_string),
          _test_string_add_char(main_string, test_string))
