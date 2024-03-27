from event import EventType
from scheduler import Scheduler
from event import Event
from interval import Interval


class TestScheduler:

    def test_add(self):
        pass

    def test_add_rand(self):
        sut = Scheduler([])
        sut.add_rand(Event(EventType.ARRIVE, 0), 1)

        got = sut.scheduler
        want = [Event(EventType.ARRIVE, 1)]

        for i, value in enumerate(got):
            assert value == want[i] 



    def test_schedule(self):
        sut = Scheduler([0.8, 0.2, 0.1])
        sut.add_rand(event=(EventType.ARRIVE, 0), rand_num=1)

        got = sut.schedule()

        print(got)
        want = 10

        for x in sut.scheduler:
            print(x)

        assert got == want

    
    def test_get_random(self):
        sut = Scheduler([0.8])

        want = 1.8
        got = sut.get_random(Interval(1, 2))

        assert got == want
