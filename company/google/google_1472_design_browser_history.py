class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

    def visit(self, url: str) -> None:
        self.history.append(url)
        # Reset forward stack
        self.future = []

    def back(self, steps: int) -> str:
        # Remove urls from history
        # Always keep at least one element in history
        # because we want to keep history stack top as current page
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future) > 0:
            self.history.append(self.future.pop())
            steps -= 1
        # history stack top is always the current page
        return self.history[-1]


if __name__ == '__main__':
    homepage = 'leetcode.com'
    obj = BrowserHistory(homepage)
    print(obj.visit('google.com'))
    print(f'  {obj.history}')
    print(obj.visit('facebook.com'))
    print(obj.visit('youtube.com'))
    print(f'  {obj.history}')
    print(obj.back(1))
    print(f'  {obj.history}')
    print(obj.back(1))
    print(f'  {obj.history}')
    print(f'  {obj.future}')
    print(obj.forward(1))
    print(f'  {obj.history}')
    print(f'  {obj.future}')
    print(obj.visit('linkedin.com'))
    print(obj.forward(2))
    print(f'  {obj.history}')
    print(f'  {obj.future}')
    print(obj.back(2))
    print(obj.back(7))
    print(f'  {obj.history}')
    print(f'  {obj.future}')
