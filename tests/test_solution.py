from solution import convert_sequence


def test_convert_sequence():
    convert_sequence("list", {"a", "c"}, [1, 2, 3]) == ["a", "c", 1, 2, 3]
    convert_sequence("tuple", ("a", "c"), [1, 2, 3]) == ("a", "c", 1, 2, 3)
    convert_sequence("set", ("a", "c"), [1, 2, 3]) == {"a", "c", 1, 2, 3}
