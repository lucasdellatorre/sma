from pseudo_random_numbers import PseudoRandomNumbers

class TestPseudoRandomNumbers:
    # def __init__(self) -> None:
    #     self.sut = PseudoRandomNumbers(1337)

    def test_gen_rand_lenght(self):
        sut = PseudoRandomNumbers(1337)
        want = 10
        got = sut.gen_rand(10)

        assert want == len(got)




