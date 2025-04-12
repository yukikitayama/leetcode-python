"""
Queue with pointer
visit
  pop from current pointer to right end
  append current url
back
  move pointer to left by min of pointer inndex or steps
forward
  move pointer to right by min of (queue length - pointer index - 1) or steps
"""

import collections


class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.curr = 0
        self.right = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.urls):
            self.urls[self.curr] = url
        else:
            self.urls.append(url)
        self.right = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.urls[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.right, self.curr + steps)
        return self.urls[self.curr]


class BrowserHistor1:

    def __init__(self, homepage: str):
        self.queue = collections.deque()
        self.queue.append(homepage)
        self.idx = 0

    def visit(self, url: str) -> None:
        # i: 1, n: 3
        while self.idx < len(self.queue) - 1:
            self.queue.pop()
        self.queue.append(url)
        self.idx += 1

        # print("visit", self.queue, self.idx)

    def back(self, steps: int) -> str:
        self.idx -= min(self.idx, steps)

        # print("back", steps, self.queue, self.idx)

        return self.queue[self.idx]

    def forward(self, steps: int) -> str:
        self.idx += min(len(self.queue) - self.idx - 1, steps)

        # print("forward", steps, self.queue, self.idx)

        return self.queue[self.idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)