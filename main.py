class tree():
    class node():
        def __init__(self, left, right, leftData, rightData):
            self.left = left
            self.right = right
            self.leftData = leftData
            self.rightData = rightData

    def __init__(self):
        self.ar = [self.node(0, 1, 1, 0),
                   self.node(2, 'KeyError', 2, 0),
                   self.node(3, 4, 3, 4),
                   self.node(4, 3, 5, 6),
                   self.node('KeyError', 5, 0, 7),
                   self.node(6, 'KeyError', 8, 0),
                   self.node('KeyError', 6, 0, 9)]
        self.cur = 0

    def etch(self):
        if self.cur=="KeyError": return self.cur
        ans = self.ar[self.cur].leftData
        self.cur = self.ar[self.cur].left
        return ans

    def tag(self):
        if self.cur == "KeyError": return self.cur
        ans = self.ar[self.cur].rightData
        self.cur = self.ar[self.cur].right
        return ans


def main(data):
    ans = []
    o = tree()
    for i in data:
        if i == "tag":
            ans.append(o.tag())
        else:
            ans.append(o.etch())
    return ans


print(main(["etch", 'tag', 'etch', 'etch', 'tag', 'etch', 'tag', 'etch', 'tag', 'etch', 'tag']))