from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in
                        bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_ex():
    with pytest.raises(TypeError) as excinfo:
        fit_transform()
    assert str(excinfo.value) == 'expected at least 1 arguments, got 0'


def test_notequal():
    actual = fit_transform(['elem', 'item', 'elem', 'item', 'elem'])
    expected = [
        ('elem', [0, 1]),
        ('item', [1, 0]),
        ('elem', [0, 1]),
        ('item', [1, 0]),
        ('item', [1, 0]),
    ]
    assert actual != expected


def test_solo():
    actual = fit_transform('elem')
    expected = [
        ('elem', [1])
    ]
    assert actual == expected


def test_city():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_solo_elem():
    actual = fit_transform(['elem', 'elem', 'elem', 'elem',
                            'elem', 'elem', 'elem', 'elem', 'elem'])
    expected = [
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
        ('elem', [1]),
    ]
    assert actual == expected


if __name__ == '__main__':
    pass
