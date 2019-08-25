class ApplicationService:
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 2) + self.fib(n - 1)