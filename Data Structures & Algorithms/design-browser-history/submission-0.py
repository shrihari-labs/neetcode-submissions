class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.pointer = 0
        

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.pointer + 1]
        self.arr.append(url)
        self.pointer = len(self.arr) - 1

    def back(self, steps: int) -> str:
        val = self.pointer - steps
        if val >= 0:
            self.pointer = val
            return self.arr[val]
        else:
            self.pointer = 0
            return self.arr[0]

    def forward(self, steps: int) -> str:
        val = self.pointer + steps
        if val <= len(self.arr) - 1:
            self.pointer = val
            return self.arr[val]
        else:
            self.pointer = len(self.arr) - 1
            return self.arr[len(self.arr) - 1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)