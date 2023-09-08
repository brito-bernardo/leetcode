class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        pop_val = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return pop_val

    def top(self) -> int:
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        top_val = self.q1.pop(0)

        self.q2.append(top_val)

        self.q1, self.q2 = self.q2, self.q1

        return top_val

    def empty(self) -> bool:
        return not self.q1
