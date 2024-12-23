import pytest
from string_utils import StringUtils

str_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input, result", [
    ("microsoft", "Microsoft"),
    ("in god we trust", "In god we trust"),
    ("Строка с большой буквы", "Строка с большой буквы"),
    ("345", "345"),
    ("", ""),
    (" ", " ")
])
def test_capitilize(input, result):
    res = str_utils.capitilize(input)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("input, result", [
    ("london", "london"),
    ("better late than never", "better late than never"),
    ("Куй железо", "куй железо, пока горячо"),
    ("year 1987", "year 1987"),
    ("", "X"),
    (None, None)
])
def test_neg_capitilize(input, result):
    res = str_utils.capitilize(input)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize("input, result", [
    ("   microsoft", "microsoft"),
    (" Welcome to the machine", "Welcome to the machine"),
    ("   1 2 3 4 5", "1 2 3 4 5"),
    (" ", ""),
    ("нет пробела", "нет пробела")
])
def test_trim(input, result):
    res = str_utils.trim(input)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("input, result", [
    ("    abracadabra", " abracadabra"),
    ("  You're in the army now", "now"),
    ("   1 2 3 4 5", "1 2 3 4 5    "),
    (" ", None),
    (None, " "),
    (None, None)
])
def test_neg_trim(input, result):
    res = str_utils.trim(input)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize("input, result", [
    ("m,n,x,y", ['m', 'n', 'x', 'y']),
    ("АБВ,где,ЁЖЗ", ['АБВ', 'где', 'ЁЖЗ']),
    ("slug,is,human,readable,url",
     ['slug', 'is', 'human', 'readable', 'url']),
    ("22,33,44,55,66", ['22', '33', '44', '55', '66']),
    ("", [   ]),
    (",", ["", ""])
])
def test_tolist_comma(input, result):
    res = str_utils.to_list(input)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize("input, result, delimeter", [
    ("x,y,z", ['x', 'y', 'z'], ","),
    ("m:n:x:y", ['m', 'n', 'x', 'y'], ":"),
    ("slug-is-human-readable-url",
     ['slug', 'is', 'human', 'readable', 'url'], "-"),
    ("Текст с пробелами и датой 23.07.1645",
     ['Текст', 'с', 'пробелами', 'и', 'датой', '23.07.1645'], " "),
    ("22*33*44*55*66", ['22', '33', '44', '55', '66'], "*"),
    ("", [], ""),
    ("", [   ], ""),
    ("", [], None)
])
def test_tolist(input, result, delimeter):
    res = str_utils.to_list(input, delimeter)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("input, result", [
    ("m;n;x;y", ['m', 'n', 'x', 'y']),
    ("m, n, x, y", ['m', 'n', 'x', 'y']),
    ("slug-is-human-readable-url",
     ['slug', 'is', 'human', 'readable', 'url']),
    ("Текст с пробелами и датой 23.07.1645",
     ['Текстспробеламиидатой23071645']),
    ("22*33*44*55*66", ['115956720']),
    (None, [])
])
def test_neg_tolist_comma(input, result):
    res = str_utils.to_list(input)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("input, result, delimeter", [
    ("m,n,x,y", ['m', 'n', 'x', 'y'], ";"),
    ("m:n:x:y", ['m', 'n', 'x', 'y'], " : "),
    ("slug-is-human-readable-url",
     ['slug-', '-is-', '-human-', '-readable-', '-url'], "-"),
    ("Текст с пробелами и датой 23.07.1645",
     ['Текстспробеламиидатой23071645'], " "),
    ("22*33*44*55*66", ['115956720'], "*"),
    (None, [], ""),
    ("", None, ""),
    ("", None, None),
    (None, None, ""),
    (None, None, None)
])
def test_neg_tolist(input, result, delimeter):
    res = str_utils.to_list(input, delimeter)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "i"),
    ("slug-is-human-readable", "-"),
    ("Текст с пробелами и датой 23.07.1645", " "),
    ("56789", "7"),
    ("!@#$%^&*()_+", "%"),
    ("1", "1"),
    ("1", ""),
    ("", "")
])
def test_contains_true(string, symbol):
    res = str_utils.contains(string, symbol)
    assert res is True


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "m"),
    ("slug-is-human-readable", "_"),
    ("Текст с пробелами и датой 23.07.1645", "c"),
    ("56789", "1"),
    ("!@#$%^&*()_+", "-"),
    ("1", "0"),
    ("", "1")
])
def test_contains_false(string, symbol):
    res = str_utils.contains(string, symbol)
    assert res is False


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "MMM"),
    ("slug-is-human-readable", "---"),
    ("Текст с пробелами и датой 23.07.1645", "Текст"),
    ("56789", "56789"),
    ("!@#$%^&*()_+", "@#$"),
    (None, ""),
    ("", None),
    (None, None)
])
def test_neg_contains_true(string, symbol):
    res = str_utils.contains(string, symbol)
    assert res is True


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "mmm"),
    ("slug-is-human-readable", "___"),
    ("Текст с пробелами и датой 23.07.1645", "Тест"),
    ("56789", "56_89"),
    ("!@#$%^&*()_+", "@ $"),
    (None, ""),
    ("", None),
    (None, None)
])
def test_neg_contains_false(string, symbol):
    res = str_utils.contains(string, symbol)
    assert res is False


@pytest.mark.positive_test
@pytest.mark.parametrize("string, substr, result", [
    ("Microsoft", "Micro", 'soft'),
    ("slug-is-human-readable", "-", "slugishumanreadable"),
    ("Текст с пробелами и датой 23.07.1645", "пробелами и ",
     "Текст с датой 23.07.1645"),
    ("56789", "678", "59"),
    ("!@#$%^&*()_+", "#$%", "!@^&*()_+"),
    ("!@#$%^&*()_+", "999", "!@#$%^&*()_+"),
    ("1", "1", ""),
    ("", "", "")
])
def test_delsymbol(string, substr, result):
    res = str_utils.delete_symbol(string, substr)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("string, substr, result", [
    ("Microsoft", "micro", 'soft'),
    ("slug-is-human-readable", " ", "slugishumanreadable"),
    ("Текст с пробелами и датой 23.07.1645", "и датой 23.07.1645",
     "Текст с пробелами"),
    ("56789", "6, 7, 8", "59"),
    ("!@#$%^&*()_+", " % ", "!@#$^&*()_+"),
    ("1", "1", None),
    ("", "", None),
    (None, None, None)
])
def test_neg_delsymbol(string, substr, result):
    res = str_utils.delete_symbol(string, substr)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "M"),
    ("slug-is-human-readable", "s"),
    ("текст с пробелами и датой 23.07.1645", "т"),
    ("56789", "5"),
    ("!@#$%^&*()_+", "!"),
    ("1", "1"),
    ("     ", " "),
    ("   ", ""),
    ("None", "")
])
def test_starts_with_true(string, symbol):
    res = str_utils.starts_with(string, symbol)
    assert res is True


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "i"),
    ("slug-is-human-readable", "e"),
    ("текст с пробелами и датой 23.07.1645", "T"),
    ("56789", "2"),
    ("!@#$%^&*()_+", " !"),
    ("None", " ")
])
def test_starts_with_false(string, symbol):
    res = str_utils.starts_with(string, symbol)
    assert res is False


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "Micro"),
    ("slug-is-human-readable", "sss"),
    ("текст с пробелами и датой 23.07.1645", "текст"),
    ("56789", "56789"),
    ("56789", "54321"),
    ("!@#$%^&*()_+", "! ! !"),
    ("1", "111"),
    (" ", " 1 "),
    ("", None),
    (None, None)
])
def test_neg_starts_with_true(string, symbol):
    res = str_utils.starts_with(string, symbol)
    assert res is True


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "mmm"),
    ("slug-is-human-readable", "-is-"),
    ("текст с пробелами и датой 23.07.1645", "23.07.1645"),
    ("56789", "98765"),
    ("!@#$%^&*()_+", "+++"),
    ("1", "231"),
    ("", " "),
    (None, "")
])
def test_neg_starts_with_false(string, symbol):
    res = str_utils.starts_with(string, symbol)
    assert res is False


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "t"),
    ("slug-is-human-readable", "e"),
    ("текст с пробелами и датой 23.07.1645", "5"),
    ("56789", "9"),
    ("!@#$%^&*()_+", "+"),
    ("empty tail", ""),
    ("1", "1"),
    ("     ", " "),
    ("   ", "")
])
def test_ends_with_true(string, symbol):
    res = str_utils.ends_with(string, symbol)
    assert res is True


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "T"),
    ("slug-is-human-readable", "s"),
    ("текст с пробелами и датой 23.07.1645", "т"),
    ("56789", "7"),
    ("!@#$%^&*()_+", "$"),
    ("1", "2"),
    ("     ", "_")
])
def test_ends_with_false(string, symbol):
    res = str_utils.ends_with(string, symbol)
    assert res is False


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "soft"),
    ("slug-is-human-readable", "eee"),
    ("текст с пробелами и датой 23.07.1645", "454545"),
    ("-56789", "-56789"),
    ("!@#$%^&*()_+", "___+++"),
    ("1", "231"),
    (" ", "     "),
    (" ", " 1 "),
    (None, ""),
    (None, None)
])
def test_neg_ends_with_true(string, symbol):
    res = str_utils.ends_with(string, symbol)
    assert res is True


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("string, symbol", [
    ("Microsoft", "Micro"),
    ("slug-is-human-readable", "---"),
    ("текст с пробелами и датой 23.07.1645", "текст с пробелами"),
    ("56789", "98765"),
    ("!@#$%^&*()_+", "$%^&@"),
    ("1", "132"),
    ("   ", "___"),
    ("", None)
])
def test_neg_ends_with_false(string, symbol):
    res = str_utils.ends_with(string, symbol)
    assert res is False


@pytest.mark.positive_test
@pytest.mark.parametrize("string", ["", " ", "       "])
def test_empty_true(string):
    res = str_utils.is_empty(string)
    assert res is True


@pytest.mark.positive_test
@pytest.mark.parametrize("string", [
    "_", "-", " None ", " 1 5 9 ", "!@#$%^&*+", "\"\""
    ])
def test_empty_false(string):
    res = str_utils.is_empty(string)
    assert res is False


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("string", [None, [], [   ]])
def test_neg_empty_true(string):
    res = str_utils.is_empty(string)
    assert res is True


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("string", [[1, 2, 3], ("a", "b", "c")])
def test_neg_empty_false(string):
    res = str_utils.is_empty(string)
    assert res is False


@pytest.mark.positive_test
@pytest.mark.parametrize("list, string", [
    ([10, 9, 8, 7], "10, 9, 8, 7"),
    (['a', 'b', 'c'], "a, b, c"),
    ([], ""),
    ([[], [], []], "[], [], []")
    ])
def test_list_comma_string(list, string):
    res = str_utils.list_to_string(list)
    assert res == string


@pytest.mark.positive_test
@pytest.mark.parametrize("list, joiner, string", [
    ([10, 9, 8, 7], "; ", "10; 9; 8; 7"),
    (['a', 'b', 'c'], " * ", "a * b * c"),
    (['state', 'of', 'the', 'art'], "-", "state-of-the-art"),
    (['', 'бр', 'к', 'д', 'бр', ''], "а", "абракадабра"),
    ([], "!!!", ""),
    ([[], [], []], "[]", "[][][][][]")
    ])
def test_list_string(list, joiner, string):
    res = str_utils.list_to_string(list, joiner)
    assert res == string


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("list, string", [
    ([10, 9, 8, 7], "10987"),
    (['a', 'b', 'c'], "a * b * c"),
    (['X', 'Y', 'Z', '@'], "x, y, z, @"),
    (['state', 'of', 'the', 'art'], "state of the art"),
    (['а', 'бр', 'а', 'к', 'а', 'д', 'а', 'бр', 'а'], "абракадабра"),
    (['a'], "a,"),
    ([], ""),
    ([None], ""),
    (None, ""),
    (None, None)
    ])
def test_neg_list_comma_string(list, string):
    res = str_utils.list_to_string(list)
    assert res == string


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
@pytest.mark.parametrize("list, joiner, string", [
    ([10, 9, 8, 7], "", "10, 9, 8, 7"),
    (['a', 'b', 'c'], "*", "a * b * c"),
    (['X', 'Y', 'Z', '@'], " / ", "x / y / z / 2"),
    (['state', 'of', 'the', 'art'], "", "state-of-the-art"),
    (['бр', 'к', 'д', 'бр'], "а", "абракадабра"),
    ([], " ", ""),
    ([None], " ", ""),
    (None, "", ""),
    (None, None, ""),
    (None, None, None)
    ])
def test_neg_list_string(list, joiner, string):
    res = str_utils.list_to_string(list, joiner)
    assert res == string
