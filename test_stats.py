from stats import Stats
from queue_1 import Queue

class TestStats:
    def queue(self):
        queue = Queue(capacity=5, servers=0, scheduler=None, arrival_interval=None, service_interval=None)
        queue.states = [3.500000000000001, 6.9999999999999964, 2.0, 0, 0, 0]
        queue.global_time = 12.5
        return queue

    def test_calc_prob_distribution(self):
        queue = self.queue()
        sut = Stats(queue)
        got = sut.calc_prob_distribution()
        want = [(0, 3.500000000000001, 0.2800000000000001), (1, 6.9999999999999964, 0.5599999999999997), (2, 2.0, 0.16), (3, 0, 0.0), (4, 0, 0.0), (5, 0, 0.0)]

        assert got == want