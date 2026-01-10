# pylint: skip-file

import unittest


from qaekwy.core.model.cutoff import (
    Cutoff,
    CutoffConstant,
    CutoffFibonacci,
    CutoffGeometric,
    CutoffLuby,
    CutoffLinear,
    CutoffRandom,
    MetaCutoffAppender,
    MetaCutoffMerger,
    MetaCutoffRepeater,
)



class TestCutoff(unittest.TestCase):

    def test_cutoff_constant(self):
        c = CutoffConstant(42)

        assert c.constant_value == 42
        assert c.is_meta() is False
        assert c.to_json() == {"name": "constant", "value": 42}

        restored = CutoffConstant.from_json(c.to_json())
        assert restored.constant_value == 42


    def test_cutoff_fibonacci(self):
        c = CutoffFibonacci()

        assert c.is_meta() is False
        assert c.to_json() == {"name": "fibonacci"}

        restored = CutoffFibonacci.from_json({})
        assert isinstance(restored, CutoffFibonacci)


    def test_cutoff_geometric(self):
        c = CutoffGeometric(base=1.2, scale=3)

        assert c.is_meta() is False
        assert c.base == 1.2
        assert c.scale == 3

        data = c.to_json()
        restored = CutoffGeometric.from_json(data)

        assert restored.base == 1.2
        assert restored.scale == 3


    def test_cutoff_luby(self):
        c = CutoffLuby(scale=5)

        assert c.is_meta() is False
        assert c.scale == 5

        data = c.to_json()
        restored = CutoffLuby.from_json(data)

        assert restored.scale == 5


    def test_cutoff_linear(self):
        c = CutoffLinear(scale=7)

        assert c.is_meta() is False
        assert c.scale == 7

        data = c.to_json()
        restored = CutoffLinear.from_json(data)

        assert restored.scale == 7


    def test_cutoff_random(self):
        c = CutoffRandom(seed=123, minimum=10, maximum=50, round_value=5)

        assert c.is_meta() is False
        assert c.seed == 123
        assert c.minimum == 10
        assert c.maximum == 50
        assert c.round_value == 5

        data = c.to_json()
        restored = CutoffRandom.from_json(data)

        assert restored.seed == 123
        assert restored.minimum == 10
        assert restored.maximum == 50
        assert restored.round_value == 5

    def test_meta_cutoff_appender(self):
        first = CutoffConstant(10)
        second = CutoffLinear(3)

        meta = MetaCutoffAppender(
            first_cutoff=first,
            number_from_first=2,
            second_cutoff=second,
        )

        assert meta.is_meta() is True
        assert meta.number_from_first == 2

        data = meta.to_json()
        restored = MetaCutoffAppender.from_json(data)

        assert isinstance(restored.first_cutoff, CutoffConstant)
        assert isinstance(restored.second_cutoff, CutoffLinear)
        assert restored.number_from_first == 2


    def test_meta_cutoff_merger(self):
        first = CutoffConstant(5)
        second = CutoffFibonacci()

        meta = MetaCutoffMerger(first, second)

        assert meta.is_meta() is True

        data = meta.to_json()
        restored = MetaCutoffMerger.from_json(data)

        assert isinstance(restored.first_cutoff, CutoffConstant)
        assert isinstance(restored.second_cutoff, CutoffFibonacci)


    def test_meta_cutoff_repeater(self):
        sub = CutoffGeometric(base=2.0, scale=3)
        meta = MetaCutoffRepeater(sub_cutoff=sub, repeat=4)

        assert meta.is_meta() is True
        assert meta.repeat == 4

        data = meta.to_json()
        restored = MetaCutoffRepeater.from_json(data)

        assert isinstance(restored.sub_cutoff, CutoffGeometric)
        assert restored.repeat == 4

    def test_nested_meta_cutoffs_roundtrip(self):
        base = CutoffConstant(10)
        repeated = MetaCutoffRepeater(base, repeat=3)
        merged = MetaCutoffMerger(repeated, CutoffLinear(2))

        data = merged.to_json()
        restored = Cutoff.from_json(data)

        assert isinstance(restored, MetaCutoffMerger)
        assert isinstance(restored.first_cutoff, MetaCutoffRepeater)
        assert isinstance(restored.first_cutoff.sub_cutoff, CutoffConstant)
        assert restored.first_cutoff.repeat == 3
        assert isinstance(restored.second_cutoff, CutoffLinear)


if __name__ == "__main__":
    unittest.main()
