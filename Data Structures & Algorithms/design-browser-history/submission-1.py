class BrowserHistory:
    #Dynamic Array method
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.curr + 1]
        self.arr.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr-steps)
        return self.arr[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.arr)-1, self.curr + steps)
        return self.arr[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)