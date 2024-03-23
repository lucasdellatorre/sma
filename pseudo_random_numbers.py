class PseudoRandomNumbers:
    def __init__(self, seed) -> None:
        self.m = 2**28
        self.a = 1317293
        self.c = 12309820398
        self.seed = seed

    def gen_rand(self, n):
        x = self.seed #seed
        arr = []
        for _ in range(n):
            op = (self.a * x + self.c) % self.m
            x = op
            arr.append(op/self.m)
        return arr
    
