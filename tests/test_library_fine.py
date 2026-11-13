import pytest

from library_fine import calculate_fine


@pytest.mark.parametrize("days_overdue, expected", [
    (0, 0),
    (1, 50),
    (5, 250),
    (9, 450),
    (10, 500),
    (11, 550),
    (20, 1000),
])
def test_calculate_fine_returns_fine_in_integer_cents(days_overdue, expected):
    result = calculate_fine(days_overdue)

    assert result == expected
    assert type(result) is int


def test_calculate_fine_rejects_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-1)


@pytest.mark.parametrize("days_overdue", [1.5, "1", None, True])
def test_calculate_fine_rejects_invalid_types(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
