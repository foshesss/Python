def two_sum(li, target):
    map = {}

    for i, elem in enumerate(li):
        diff = target - elem
        if diff in map:
            return [i, map[diff]]
        map[elem] = i

    return []

print(two_sum([1, 2, 3, 4, 5, 6, 7, 8], 14))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, p):
        return abs(p.x - self.x) + abs(p.y - self.y)

    def print(self):
        print(f"({self.x}, {self.y})")

def valid_parenthesis(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')' and len(stack) != 0:
            stack.pop()
        else:
            return False

    return len(stack) == 0

p1 = Point(1, 5)
p2 = Point(5, 1)

print(p2.dist(p1))

print(valid_parenthesis("((())()(()))"))



