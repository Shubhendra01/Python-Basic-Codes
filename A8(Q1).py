class p(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
p1 = p(1,4)
p2 = p(2,5)
print(p1.show())
print(p2.show())
p1.move(5,6)
p2.move(7,8)
print(p1.show())
print(p2.show())
