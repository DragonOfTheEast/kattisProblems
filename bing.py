class Node:
    def __init__(self):
        self.touched = 0
        self.children = [None]*26

def _insert_word(word):
    temp = head
    ans = 0
    for char in enumerate(word):
        child_index = ord(char) - ord('a')

        if temp.children[child_index] is None:
            temp.children[child_index] = Node()

        ans = temp.children[child_index].touched
        temp.children[child_index].touched += 1
        temp = temp.children[child_index]
    return ans

n = int(input())
head = Node()
for i in range(n):
    word = input()
    print(_insert_word(word))

