import sys
#use a linked list
#the head will be the last first index we see
class Node:
    def __init__(self, string):
        self.string = string
        self.next = None
        self.tail = self

    def insert(self,other):
        self.tail.next = other
        self.tail = other.tail

    def get_answer(self):
        temp = self
        while temp.next is not None:
            sys.stdout.write(temp.string)
            temp = temp.next
        sys.stdout.write(temp.string + '\n')

lines = sys.stdin.read().splitlines()
n = int(lines[0])

arr = [Node(lines[i+1]) for i in range(n)]
head = arr[0]
for line in lines[n+1:]:
    a,b = map(int, line.split())
    a -= 1
    b -= 1
    arr[a].insert(arr[b])
    head = arr[a]

head.get_answer()
