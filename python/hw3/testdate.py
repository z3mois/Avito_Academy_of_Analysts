from unittest.mock import patch
from date import what_is_year_now
import pytest
import io


def test_first():
    with patch("date.urllib.request.urlopen") as mocked_get_cases:
        data = io.StringIO('{"currentDateTime": "2019-03-01"}')
        mocked_get_cases.return_value = data
        assert what_is_year_now() == 2019
        mocked_get_cases.assert_called_once()


def test_second():
    with patch("date.urllib.request.urlopen") as mocked_get_cases:
        data = io.StringIO('{"currentDateTime": "01.03.2019"}')
        mocked_get_cases.return_value = data
        assert what_is_year_now() == 2019
        mocked_get_cases.assert_called_once()


def test_nothing():
    with patch("date.urllib.request.urlopen") as mocked_get_cases:
        data = io.StringIO('{"currentDateTime": "01.032019"}')
        mocked_get_cases.return_value = data
        with pytest.raises(ValueError) as excinfo:
            what_is_year_now()
        assert str(excinfo.value) == 'Invalid format'
        mocked_get_cases.assert_called_once()


if __name__ == '__main__':
    pass
