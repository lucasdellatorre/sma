class PseudoRandomNumbers:
    def __init__(self, seed, total_numbers, random_numbers = None, generate=False) -> None:
        self.m = 2**28
        self.a = 1317293
        self.c = 12309820398
        self.seed = seed

        self.x = seed
        self.total_numbers = total_numbers

        self.numbers = random_numbers
        self.generate = generate

        if generate == False:
            self.total_numbers = len(random_numbers)

        self.current = -1

    def gen_rand(self, n):
        x = self.seed #seed
        arr = []
        for _ in range(n):
            if _ % 10000000 == 0: print(_)
            op = (self.a * x + self.c) % self.m
            x = op
            arr.append(op/self.m)
        return arr
    
    def get_next_number(self):
        self.current += 1
        if self.numbers and not self.generate:
            return self.numbers[self.current % self.total_numbers]
        op = (self.a * self.x + self.c) % self.m
        self.x = op
        return op/self.m
    
    def reset(self):
        self.x = self.seed
        self.current = -1