from magic_passes import MagicPasses


def test_is_multiple_of_three():
    magic_passes = MagicPasses()

    assert magic_passes._is_multiple_of_three(9)
    assert magic_passes._is_multiple_of_three(27)


def test_is_not_multiple_of_three():
    magic_passes = MagicPasses()

    assert not magic_passes._is_multiple_of_three(4)
    assert not magic_passes._is_multiple_of_three(7)


def test_is_multiple_of_five():
    magic_passes = MagicPasses()

    assert magic_passes._is_multiple_of_five(20)
    assert magic_passes._is_multiple_of_five(55)


def test_is_not_multiple_of_five():
    magic_passes = MagicPasses()

    assert not magic_passes._is_multiple_of_five(13)
    assert not magic_passes._is_multiple_of_five(51)


def test_get_magic_count():
    magic_passes = MagicPasses()
    magic_count = magic_passes.get_magic_count(20)

    expected_magic_count = [
        1,
        2,
        "abracadabra",
        4,
        "alakazam",
        "abracadabra",
        7,
        8,
        "abracadabra",
        "alakazam",
        11,
        "abracadabra",
        13,
        14,
        "abracadabraalakazam",
        16,
        17,
        "abracadabra",
        19,
        "alakazam",
    ]

    assert magic_count == expected_magic_count
