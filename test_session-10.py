from math import pi
from Polygon_session_10 import Polygon
from PolygonSequence_session_10 import PolygonSequence
from math import pi, sin
import pytest
import random


@pytest.fixture
def generate_random_number():
    return random.randint(3, 25)


def test_polygon():
    tmp = Polygon(4, 1)
    assert tmp.interior_angle == 90  # interior angle of a square


def test_polygon_eq():
    tmp1 = Polygon(10, 2)
    tmp2 = Polygon(10, 2)

    assert tmp1 == tmp2


def test_polygon_gt():
    tmp1 = Polygon(10, 2)
    tmp2 = Polygon(4, 2)

    assert tmp1 > tmp2


def test_polygon_edge_bad_input():
    with pytest.raises(ValueError):
        _ = Polygon("10", 3)


def test_polygon_radius_bad_input():
    with pytest.raises(ValueError):
        _ = Polygon(10, -2)


def test_polygon_update_edges():
    tmp = Polygon(3, 1)
    assert tmp.interior_angle == 60

    tmp.edges = 5
    assert tmp.interior_angle == 108


def test_polyseq():
    tmp = PolygonSequence(10, 1)
    assert tmp.max_edge == 10
    assert len(tmp[:]) == 8  # (since we begin creating polygon with n=3 onwards)


def test_polyseq_len(generate_random_number):
    tmp = PolygonSequence(generate_random_number, 5)
    assert len(tmp) == generate_random_number - 2


def test_polyseq_max_efficiency():
    temp = PolygonSequence(25, 5)
    assert temp.max_efficiency.edges == 25


def test_polyseq_wrong_start():
    tmp = PolygonSequence(10, 4)
    assert len(tmp) == 8


def test_polyseq_reverse_index():
    tmp = PolygonSequence(25, 2)
    assert len(tmp[::-1]) == 23
