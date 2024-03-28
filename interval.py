class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f'Start {self.start} | End {self.end}'
