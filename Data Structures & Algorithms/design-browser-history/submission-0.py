class ListNode:
    def __init__(self, homepage, prev=None, next=None):
        self.homepage = homepage
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:

        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.homepage

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)