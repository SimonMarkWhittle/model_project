
from modproj.numberstreamator import Numberstreamator

def test_module_numberstream():
    import random
    random.seed = 8675309

    numberstream = Numberstreamator(
        streamcount=10,
    )

    res = numberstream.stream_numbers()

    assert len(res) == 10


if __name__ == '__main__':
    test_module_numberstream()
