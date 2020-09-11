from math import ceil
import random
from datetime import datetime
random.seed(datetime.now())
a, b = [int(i) for i in input().split()]

def get_random_word():
    length = random.randint(1,15)
    word =""

    for i in range(length):
        word += chr(random.randint(97,122))
    return word


def did_it_add(ret:set):
    return len(ret) != (ret.add(get_random_word()) or len(ret))


ret = set()

if b/2 > a:
    i = 0
    while i < (ceil(b/2)):
        if did_it_add(ret):
            i += 1
else:
    i = 0
    while i < a:
        if did_it_add(ret):
            i += 1

print(" ".join(_ for _ in list(ret)))